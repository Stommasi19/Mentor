"""Local interview records using the same neutral project identity as preferences."""

from datetime import date
from pathlib import Path
import re

from runtime.preferences import resolve_data_root


class InterviewArtifacts:
    """Reserve separate task records; never write preferences or select a fallback root."""

    def __init__(self, data_root: str, project_id: str):
        if not re.fullmatch(r"[0-9a-f]{64}", project_id):
            raise ValueError("project identity is unavailable or invalid")
        self.plans = resolve_data_root(data_root) / "projects" / project_id / "plans"

    def create(self, task: str) -> Path:
        if not task.strip():
            raise ValueError("task must not be empty")
        slug = re.sub(r"[^a-z0-9]+", "-", task.lower()).strip("-")[:64].rstrip("-") or "interview"
        name = f"{date.today().isoformat()}-{slug}"
        self.plans.mkdir(parents=True, exist_ok=True)
        suffix = 1
        while True:
            directory = self.plans / (name if suffix == 1 else f"{name}-{suffix}")
            try:
                # Exclusive mkdir prevents two interviews from sharing a transcript.
                directory.mkdir()
                break
            except FileExistsError:
                suffix += 1
        try:
            (directory / "interview.md").write_text("# Interview record\n", encoding="utf-8")
        except OSError:
            directory.rmdir()
            raise
        return directory

    def locate(self, directory: str) -> Path:
        path = Path(directory)
        if not path.is_absolute():
            raise ValueError("artifact directory must be absolute")
        path = path.resolve(strict=True)
        if path.parent != self.plans.resolve() or not path.is_dir():
            raise ValueError("artifact directory must belong to this project's plans")
        if not (path / "interview.md").is_file():
            raise ValueError("interview record is missing")
        return path

    def append(self, directory: str, markdown: str) -> Path:
        if not markdown.strip():
            raise ValueError("interview entry must not be empty")
        record = self.locate(directory) / "interview.md"
        with record.open("a", encoding="utf-8") as stream:
            stream.write("\n" + markdown + "\n")
        return record

    def finalize(self, directory: str, confirmation: str, plan: str) -> Path:
        if not confirmation.strip() or not plan.strip():
            raise ValueError("confirmation and plan must not be empty")
        path = self.locate(directory)
        # Two Markdown files are not a transaction. A failure remains visible;
        # the caller inspects partial records before retrying or handing off.
        self.append(directory, "## Confirmation\n\n" + confirmation)
        plan_path = path / "plan.md"
        plan_path.write_text(plan, encoding="utf-8")
        return plan_path
