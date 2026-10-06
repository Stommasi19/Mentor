#!/usr/bin/env python3
"""Print a local hooks.json; configuration review and trust remain host actions."""

import json
from pathlib import Path
import shlex
import sys


def main() -> None:
    handler = Path(__file__).resolve().with_name("session_start.py")
    # The native host executes a shell command. Quote both paths, including the
    # interpreter, rather than relying on the session's directory or PATH.
    command = shlex.join([sys.executable, str(handler)])
    configuration = {
        "description": "Mentor local development policy and preferences hook",
        "hooks": {
            "SessionStart": [
                {
                    "matcher": "^(startup|resume|clear|compact)$",
                    "hooks": [
                        {
                            "type": "command",
                            "command": command,
                            "timeout": 10,
                            "additionalContextLimit": 5000,
                            "statusMessage": "Loading Mentor policy and project defaults",
                        }
                    ],
                }
            ]
        },
    }
    json.dump(configuration, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
