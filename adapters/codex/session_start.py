#!/usr/bin/env python3
"""Deliver the canonical Mentor policy through Codex's SessionStart contract."""

import json
from pathlib import Path
import sys


def main() -> int:
    try:
        event = json.load(sys.stdin)
        if not isinstance(event, dict) or event.get("hook_event_name") != "SessionStart":
            raise ValueError("expected a SessionStart event")
        if event.get("source") not in ("startup", "resume", "clear", "compact"):
            raise ValueError("expected source startup, resume, clear, or compact")

        # Hooks run in the learner's workspace. Locate resources beside this
        # adapter, so changing that workspace cannot select a different policy.
        policy_path = Path(__file__).resolve().parents[2] / "core" / "policy.md"
        policy = policy_path.read_text(encoding="utf-8").strip()
        if not policy:
            raise ValueError(f"core policy is empty: {policy_path}")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Mentor SessionStart failed: {error}", file=sys.stderr)
        return 1

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": policy,
            }
        },
        sys.stdout,
        ensure_ascii=False,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
