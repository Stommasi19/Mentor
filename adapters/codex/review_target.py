#!/usr/bin/env python3
"""Read-only Git and GitHub snapshots; host transport stays outside Mentor core."""

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
from urllib.parse import quote


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def content(data: bytes, mode: str, blob: str | None = None) -> dict:
    result = {"mode": mode, "sha256": digest(data), "git_blob": blob}
    try:
        result["text"] = data.decode("utf-8")
    except UnicodeError:
        result["base64"] = base64.b64encode(data).decode("ascii")
    return result


def run(command: list[str], cwd: Path | None = None) -> bytes:
    environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    environment.update({"LC_ALL": "C", "GIT_OPTIONAL_LOCKS": "0", "GH_PROMPT_DISABLED": "1"})
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, timeout=60)
    if result.returncode:
        raise ValueError(result.stderr.decode("utf-8", errors="replace").strip() or "target command failed")
    return result.stdout


class LocalTarget:
    def __init__(self, workspace: str):
        if not Path(workspace).is_absolute():
            raise ValueError("workspace must be absolute")
        root = self.git_at(Path(workspace), "rev-parse", "--show-toplevel")
        self.root = Path(os.fsdecode(root.removesuffix(b"\n"))).resolve(strict=True)

    @staticmethod
    def git_at(root: Path, *args: str) -> bytes:
        # Literal pathspecs prevent filenames like '[draft]' selecting other files.
        # Disabling external diff/textconv prevents checkout-controlled commands.
        return run(["git", "--literal-pathspecs", "-c", "core.fsmonitor=false", "-C", str(root), *args])

    def git(self, *args: str) -> bytes:
        return self.git_at(self.root, *args)

    def revision(self, ref: str) -> str:
        return self.git("rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()

    def blob(self, oid: str, mode: str) -> dict | None:
        if mode == "000000":
            return None
        if mode == "160000":
            return {"mode": mode, "git_blob": oid, "submodule_commit": oid}
        return content(self.git("cat-file", "blob", oid), mode, oid)

    def working_content(self, filename: str) -> dict | None:
        path = self.root / filename
        # A replaced parent directory must not redirect a source read outside
        # the reviewed checkout. A symlink file itself is captured as link text.
        for parent in path.parents:
            if parent == self.root:
                break
            if parent.is_symlink():
                raise ValueError(f"source parent is a symlink: {filename}")
        try:
            info = path.lstat()
        except FileNotFoundError:
            return None
        if stat.S_ISLNK(info.st_mode):
            return content(os.fsencode(os.readlink(path)), "120000")
        if stat.S_ISREG(info.st_mode):
            return content(path.read_bytes(), "100755" if info.st_mode & 0o111 else "100644")
        if stat.S_ISDIR(info.st_mode):
            # Status filenames do not identify dirty submodule contents. Review
            # those as a separate target rather than claim a stable snapshot.
            head = self.git_at(path, "rev-parse", "HEAD").decode().strip()
            dirty = self.git_at(path, "status", "--porcelain=v1", "-z")
            if dirty:
                raise ValueError(f"dirty submodule requires a separate local target: {filename}")
            return {"mode": "160000", "submodule_commit": head}
        raise ValueError(f"unsupported file type: {filename}")

    def changes(self, args: list[str], layer: str, paths: list[str], working: bool) -> dict:
        options = ["--no-ext-diff", "--no-textconv", "--find-renames"]
        tokens = self.git("diff", *options, "--raw", "--no-abbrev", "-z", *args, "--", *paths).split(b"\0")
        entries = []
        index = 0
        while index < len(tokens) and tokens[index]:
            modes = tokens[index].decode("ascii").removeprefix(":").split()
            old_mode, new_mode, old_oid, new_oid, status_code = modes
            old_path = os.fsdecode(tokens[index + 1])
            index += 2
            filename = old_path
            if status_code[0] in "RC":
                filename = os.fsdecode(tokens[index])
                index += 1
            after = self.working_content(filename) if working else self.blob(new_oid, new_mode)
            entries.append({"layer": layer, "status": status_code, "old_path": old_path,
                            "path": filename, "before": self.blob(old_oid, old_mode), "after": after})
        patch = self.git("diff", *options, "--binary", *args, "--", *paths).decode("utf-8", errors="replace")
        return {"layer": layer, "diff": patch, "entries": entries}

    def capture(self, scope: str, base: str | None = None, head: str = "HEAD",
                paths: list[str] | None = None) -> dict:
        paths = paths or []
        for name in paths:
            if not name or PurePosixPath(name).is_absolute() or ".." in PurePosixPath(name).parts:
                raise ValueError("selected paths must be relative to the repository")
        current_head = self.revision("HEAD")
        layers = []
        if scope == "range":
            if not base:
                raise ValueError("range scope requires an explicit base")
            resolved_head = self.revision(head)
            resolved_base = self.revision(base)
            # PR-style branch changes start at the common ancestor.
            ancestor = self.git("merge-base", resolved_base, resolved_head).decode().strip()
            layers.append(self.changes([ancestor, resolved_head], "range", paths, False))
        elif scope in ("uncommitted", "staged", "unstaged"):
            resolved_base = self.revision(base or "HEAD")
            resolved_head = current_head
            ancestor = None
            if scope in ("uncommitted", "staged"):
                layers.append(self.changes(["--cached", resolved_base], "staged", paths, False))
            if scope in ("uncommitted", "unstaged"):
                layers.append(self.changes([], "unstaged", paths, True))
            if scope == "uncommitted":
                names = self.git("ls-files", "--others", "--exclude-standard", "-z", "--", *paths)
                entries = [{"layer": "untracked", "status": "A", "old_path": None,
                            "path": os.fsdecode(name), "before": None,
                            "after": self.working_content(os.fsdecode(name))}
                           for name in names.split(b"\0") if name]
                layers.append({"layer": "untracked", "diff": "", "entries": entries})
        else:
            raise ValueError("select uncommitted, staged, unstaged or range scope")
        payload = {"kind": "local", "workspace": str(self.root), "scope": scope,
                   "requested_paths": paths, "base": resolved_base, "head": resolved_head,
                   "checkout_head": current_head, "merge_base": ancestor, "layers": layers}
        payload["included_paths"] = sorted({entry[key] for layer in layers for entry in layer["entries"]
                                            for key in ("path", "old_path") if entry[key]})
        payload["snapshot_id"] = digest(json.dumps(payload, sort_keys=True, ensure_ascii=True).encode())
        return payload


def parse_pr(url: str) -> tuple[str, int]:
    match = re.fullmatch(r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/pull/([1-9][0-9]*)/?", url)
    if not match:
        raise ValueError("supply an explicit GitHub pull-request URL")
    return match[1], int(match[2])


class GitHubTransport:
    """Read-only gh transport, including paginated filenames and pinned file contents."""

    def api(self, endpoint: str, *options: str) -> bytes:
        return run(["gh", "api", "--hostname", "github.com", "--method", "GET", endpoint, *options])

    def merge_base(self, repository: str, base: str, head: str, head_repository: str) -> str:
        comparison_head = f"{head_repository.split('/')[0]}:{head}"
        response = json.loads(self.api(f"repos/{repository}/compare/{base}...{comparison_head}"))
        return response["merge_base_commit"]["sha"]

    def metadata(self, repository: str, number: int) -> dict:
        return json.loads(self.api(f"repos/{repository}/pulls/{number}"))

    def diff(self, repository: str, number: int) -> str:
        return self.api(f"repos/{repository}/pulls/{number}", "-H",
                        "Accept: application/vnd.github.diff").decode("utf-8")

    def files(self, repository: str, number: int) -> list[dict]:
        pages = json.loads(self.api(f"repos/{repository}/pulls/{number}/files?per_page=100",
                                   "--paginate", "--slurp"))
        return [item for page in pages for item in page]

    def file(self, repository: str, revision: str, path: str) -> dict:
        response = json.loads(self.api(f"repos/{repository}/contents/{quote(path, safe='/')}?ref={revision}"))
        if response.get("encoding") != "base64" or response.get("type") != "file":
            raise ValueError(f"file context unavailable: {path}; use a pinned disposable checkout")
        return content(base64.b64decode(response["content"]), "remote", response.get("sha"))


def pr_revisions(metadata: dict, repository: str, number: int) -> tuple[str, str, str]:
    if metadata["number"] != number or metadata["base"]["repo"]["full_name"].lower() != repository.lower():
        raise ValueError("PR metadata does not match the requested repository/number")
    base, head = metadata["base"]["sha"], metadata["head"]["sha"]
    if not all(isinstance(ref, str) and re.fullmatch(r"[0-9a-f]{40,64}", ref) for ref in (base, head)):
        raise ValueError("PR metadata lacks exact base/head revisions")
    return base, head, metadata["head"]["repo"]["full_name"]


def capture_pr(url: str, transport: GitHubTransport | None = None) -> dict:
    repository, number = parse_pr(url)
    transport = transport or GitHubTransport()
    first = transport.metadata(repository, number)
    base, head, head_repository = pr_revisions(first, repository, number)
    merge_base = transport.merge_base(repository, base, head, head_repository)
    if not isinstance(merge_base, str) or not re.fullmatch(r"[0-9a-f]{40,64}", merge_base):
        raise ValueError("PR comparison lacks an exact merge-base revision")
    patch = transport.diff(repository, number)
    files = transport.files(repository, number)
    if len(files) != first["changed_files"]:
        raise ValueError("PR file list is incomplete; use a pinned disposable checkout")
    entries = []
    for item in files:
        filename, status_code = item["filename"], item["status"]
        old = item.get("previous_filename", filename)
        entries.append({"path": filename, "old_path": old, "status": status_code,
            "before": None if status_code == "added" else transport.file(repository, merge_base, old),
            "after": None if status_code == "removed" else transport.file(head_repository, head, filename)})
    final = transport.metadata(repository, number)
    if pr_revisions(final, repository, number) != (base, head, head_repository):
        raise ValueError("PR changed during retrieval; refresh the target before using this evidence")
    payload = {"kind": "pr", "url": f"https://github.com/{repository}/pull/{number}",
        "repository": repository, "head_repository": head_repository, "base": base, "head": head,
        "merge_base": merge_base,
        "title": first.get("title", ""), "description": first.get("body", ""),
        "diff": patch, "entries": entries, "included_paths": [entry["path"] for entry in entries]}
    payload["snapshot_id"] = digest(json.dumps(payload, sort_keys=True, ensure_ascii=True).encode())
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    targets = parser.add_subparsers(dest="kind", required=True)
    local = targets.add_parser("local")
    local.add_argument("--workspace", required=True)
    local.add_argument("--scope", choices=("uncommitted", "staged", "unstaged", "range"), required=True)
    local.add_argument("--base")
    local.add_argument("--head", default="HEAD")
    local.add_argument("--path", action="append", default=[])
    pr = targets.add_parser("pr")
    pr.add_argument("--url", required=True)
    args = parser.parse_args()
    try:
        if args.kind == "local":
            target = LocalTarget(args.workspace)
            result = target.capture(args.scope, args.base, args.head, args.path)
            # Changes during capture are rejected rather than called a stable snapshot.
            if target.capture(args.scope, args.base, args.head, args.path)["snapshot_id"] != result["snapshot_id"]:
                raise ValueError("local target changed during capture; retry")
        else:
            result = capture_pr(args.url)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, RuntimeError,
            subprocess.SubprocessError) as error:
        print(f"Mentor target failed: {error}", file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
