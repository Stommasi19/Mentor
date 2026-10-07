#!/usr/bin/env python3
"""Resolve development skill resources and read-only M02 state for native invocation."""

import argparse
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

REPOSITORY = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPOSITORY))
from runtime.preferences import PreferenceStore, control, resolve_data_root, resolve_project


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--data-root")
    parser.add_argument("--session", default="{}")
    arguments = parser.parse_args()
    try:
        if not Path(arguments.workspace).is_absolute():
            raise ValueError("workspace must be absolute")
        project_id = resolve_project(arguments.workspace)
        configured = arguments.data_root if arguments.data_root is not None else os.environ.get(
            "MENTOR_DATA_DIR", str(Path.home() / ".mentor"))
        data_root = str(resolve_data_root(configured))
        resources = {
            "policy_path": REPOSITORY / "core" / "policy.md",
            "workflow_path": REPOSITORY / "core" / "workflows" / "interview.md",
        }
        for path in resources.values():
            if not path.read_text(encoding="utf-8").strip():
                raise ValueError(f"Mentor resource is empty: {path}")
        status = control(PreferenceStore(data_root, project_id), session=json.loads(arguments.session))
        adapter = REPOSITORY / "adapters" / "codex"
        locations = ["--project-id", project_id, "--data-root", data_root]
        result = {
            **{name: str(path) for name, path in resources.items()},
            "project_id": project_id, "data_root": data_root, "status": status,
            "control_command": shlex.join([sys.executable, str(adapter / "control.py"), *locations]),
            "artifact_command": shlex.join([sys.executable, str(adapter / "artifacts.py"), *locations]),
        }
    except (OSError, UnicodeError, ValueError, TypeError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"Mentor interview context failed: {error}", file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
