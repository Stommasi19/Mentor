#!/usr/bin/env python3
"""Codex shell boundary for neutral reports at explicitly pinned locations."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.reports import REPORTS, ReportStore


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--data-root", required=True)
    parser.add_argument("--kind", choices=REPORTS, required=True)
    actions = parser.add_subparsers(dest="action", required=True)
    create = actions.add_parser("create")
    create.add_argument("--task", required=True)
    save = actions.add_parser("save")
    save.add_argument("--directory", required=True)
    arguments = parser.parse_args()
    try:
        store = ReportStore(arguments.data_root, arguments.project_id, arguments.kind)
        path = (store.create(arguments.task) if arguments.action == "create"
                else store.save(arguments.directory, sys.stdin.read()))
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        print(f"Mentor report failed: {error}", file=sys.stderr)
        return 1
    json.dump({"path": str(path), "persisted": True}, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
