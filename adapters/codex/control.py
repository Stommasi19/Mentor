#!/usr/bin/env python3
"""Thin Codex tool entry: explicit hook-provided locations, JSON session/result."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.preferences import PreferenceStore, control


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id")
    parser.add_argument("--data-root")
    parser.add_argument("--unavailable-reason")
    parser.add_argument("--session", default='{}', help="current conversation state as JSON")
    parser.add_argument("--scope", choices=("session", "project"), default="session")
    parser.add_argument("--field", choices=("all", "level", "coaching_enabled"), default="all")
    parser.add_argument("action", choices=("status", "set-level", "pause", "resume", "use-project", "reset"))
    parser.add_argument("value", nargs="?")
    arguments = parser.parse_args()
    try:
        result = control(
            PreferenceStore(arguments.data_root, arguments.project_id, arguments.unavailable_reason),
            arguments.action, arguments.scope, arguments.value, arguments.field,
            json.loads(arguments.session),
        )
    except (ValueError, TypeError) as error:
        print(f"Mentor control rejected: {error}", file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
