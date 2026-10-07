"""Task-specific Markdown reports, independent of host and mentoring decisions."""

from datetime import date
import json
import os
from pathlib import Path
import re
import tempfile

from runtime.preferences import resolve_data_root


REPORTS = {
    "review": ("reviews", "review.md"),
    "feedback": ("feedback", "feedback.md"),
    "pr-check": ("pr-checks", "pr-check.md"),
}


class ReportStore:
    """Reserve distinct reports and publish once, without overwriting prior work."""

    def __init__(self, data_root: str, project_id: str, kind: str):
        if not isinstance(project_id, str) or not re.fullmatch(r"[0-9a-f]{64}", project_id):
            raise ValueError("invalid project identity")
        if kind not in REPORTS:
            raise ValueError("unsupported report kind")
        self.root = resolve_data_root(data_root)
        category, self.filename = REPORTS[kind]
        self.directory = self.root / "projects" / project_id / category
        self.reservation = {"project_id": project_id, "kind": kind}

    def check_path(self, path: Path) -> None:
        """A resolved data root is allowed; redirects beneath it are not."""
        relative = path.relative_to(self.root)
        current = self.root
        for part in relative.parts:
            current /= part
            if current.is_symlink():
                raise ValueError("report paths cannot contain symlinks")

    def create(self, task: str) -> Path:
        if not isinstance(task, str) or not task.strip():
            raise ValueError("task must not be empty")
        slug = re.sub(r"[^a-z0-9]+", "-", task.lower()).strip("-")[:64].rstrip("-") or "report"
        name = f"{date.today().isoformat()}-{slug}"
        self.check_path(self.directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        suffix = 1
        while True:
            path = self.directory / (name if suffix == 1 else f"{name}-{suffix}")
            try:
                path.mkdir()
                break
            except FileExistsError:
                suffix += 1
        try:
            # A second process can verify that create reserved this directory.
            (path / ".reservation.json").write_text(json.dumps(self.reservation), encoding="utf-8")
        except OSError:
            path.rmdir()
            raise
        return path

    def locate(self, directory: str) -> Path:
        path = Path(directory)
        if not path.is_absolute() or path.parent != self.directory or not path.is_dir():
            raise ValueError("report directory must be reserved under this project's category")
        self.check_path(path / ".reservation.json")
        if json.loads((path / ".reservation.json").read_text(encoding="utf-8")) != self.reservation:
            raise ValueError("report reservation belongs to another project or kind")
        return path

    def save(self, directory: str, markdown: str) -> Path:
        if not isinstance(markdown, str) or not markdown.strip():
            raise ValueError("report content must not be empty")
        path = self.locate(directory)
        destination = path / self.filename
        self.check_path(destination)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path, delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(markdown)
                stream.flush()
                os.fsync(stream.fileno())
            # Linking publishes complete bytes exclusively. Unlike replace(),
            # this fails if another save already owns the destination.
            os.link(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        if destination.read_text(encoding="utf-8") != markdown:
            raise ValueError("report published but persistence readback did not match")
        return destination
