#!/usr/bin/env python3
"""Codex shell entry for neutral interview artifacts at pinned hook locations."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.artifacts import InterviewArtifacts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--data-root", required=True)
    actions = parser.add_subparsers(dest="action", required=True)
    create = actions.add_parser("create")
    create.add_argument("--task", required=True)
    append = actions.add_parser("append")
    append.add_argument("--directory", required=True)
    finalize = actions.add_parser("finalize")
    finalize.add_argument("--directory", required=True)
    finalize.add_argument("--confirmation", required=True)
    arguments = parser.parse_args()
    try:
        store = InterviewArtifacts(arguments.data_root, arguments.project_id)
        if arguments.action == "create":
            path = store.create(arguments.task)
        elif arguments.action == "append":
            path = store.append(arguments.directory, sys.stdin.read())
        else:
            path = store.finalize(arguments.directory, arguments.confirmation, sys.stdin.read())
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        print(f"Mentor artifact failed: {error}", file=sys.stderr)
        return 1
    json.dump({"path": str(path), "persisted": True}, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
