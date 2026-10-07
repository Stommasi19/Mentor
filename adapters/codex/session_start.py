#!/usr/bin/env python3
"""Deliver the canonical Mentor policy through Codex's SessionStart contract."""

import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.preferences import PreferenceStore, control, resolve_data_root, resolve_project
from adapters.codex.prism.context import guidance_paths


def prism_context(event: dict) -> str:
    """Advertise optional continuity without connecting or saving at startup."""
    locations = guidance_paths(event.get('cwd'))
    return (
        '## Optional Prism project context\n' + json.dumps(locations, ensure_ascii=False) + '\n'
        'Only use Prism after explicit project-context opt-in; read the adapter guide then. '
        'Prism defaults to a dedicated Mentor database; do not load or save through '
        'Workflow’s shared Prism. Reuse a verified dedicated Prism connection and '
        'an existing Serena connection, including aliases/plugins. Do not choose '
        'another host port. When requested '
        'tools are absent, run the supplied mcp_setup_command with --apply and --server '
        'prism|serena|both; pass actual compatible connected names before setup. '
        'The host launches registered servers after reload. Save project '
        'summaries/handoffs only when requested; never save learner transcripts/grades '
        'or change Mentor preferences. Continue with local docs if unavailable. '
        'This hook performs no Prism load/save or server launch.'
    )


def interview_context() -> str:
    """Advertise explicit invocation without delivering the full workflow."""
    return (
        "## Codex explicit workflow invocation\n"
        "Full workflows run only on explicit invocation: $mentor-interview, "
        "$mentor-review, $mentor-feedback and $mentor-pr-check, "
        "registered separately through local development skill discovery. This hook "
        "does not register skills. Ordinary clarification remains available without "
        "launching that workflow. Invocation preserves effective/session/saved "
        "preferences and implementation scope."
    )


def preference_context(event: dict, adapter: Path) -> str:
    """Pin hook locations for ordinary tools, which lack hook-only environment."""
    warnings = []
    project_id = None
    data_root = None
    try:
        workspace = event.get("cwd")
        if not isinstance(workspace, str) or not Path(workspace).is_absolute():
            raise ValueError("hook workspace must be an absolute directory")
        project_id = resolve_project(workspace)
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        warnings.append(f"Project identity unavailable: {error}")
    try:
        configured = os.environ.get("MENTOR_DATA_DIR", str(Path.home() / ".mentor"))
        data_root = str(resolve_data_root(configured))
    except (OSError, ValueError, RuntimeError) as error:
        warnings.append(f"Invalid data configuration: {error}")
    reason = "; ".join(warnings) or None
    store = PreferenceStore(data_root, project_id, reason)
    status = control(store)
    command = [sys.executable, str(adapter / "control.py")]
    if reason:
        command += ["--unavailable-reason", reason]
    else:
        command += ["--project-id", project_id, "--data-root", data_root]
    lifecycle = "Start without session overrides." if event["source"] in ("startup", "clear") else (
        "Retain the conversation's session object/overrides; reload only project defaults.")
    return "\n\n".join([
        "## Mentor project defaults (not session overrides)\n" + json.dumps(status, ensure_ascii=False),
        f"Lifecycle: {event['source']}. {lifecycle}",
        "## Codex control invocation\n"
        f"Trusted workflow: {adapter.parents[1] / 'core' / 'workflows' / 'controls.md'}\n"
        f"Project ID: {project_id}; absolute data root: {data_root}.\n"
        f"Base shell command: {shlex.join(command)}\n"
        "Append --session <shell-quoted JSON of the current session object> and the action. "
        "Example initial status: append --session '{}' status. "
        "Use set-level junior|mid-level|senior (legacy aliases remain accepted), pause, resume, status, use-project "
        "(optional --field level|coaching_enabled), or --scope project reset. "
        "Only an explicit project request adds --scope project to set-level/pause/resume. "
        "Apply effective values and retain the returned session object in conversation context. "
        "Pass these exact locations even if tools run from another cwd; do not depend on hook environment. "
        "Report warnings and never claim persisted success unless persisted is true.",
    ])


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
        workflow_path = policy_path.parent / "workflows" / "controls.md"
        workflow = workflow_path.read_text(encoding="utf-8").strip()
        if not workflow:
            raise ValueError(f"controls workflow is empty: {workflow_path}")
        # Validate the advertised resource now; never claim a broken checkout
        # supplies a usable workflow. Load its instructions only when needed.
        for name in ("interview.md", "review.md", "feedback.md", "pr-understanding.md"):
            resource = policy_path.parent / "workflows" / name
            if not resource.read_text(encoding="utf-8").strip():
                raise ValueError(f"workflow is empty: {resource}")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Mentor SessionStart failed: {error}", file=sys.stderr)
        return 1

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": "\n\n".join([
                    policy, workflow, preference_context(event, Path(__file__).resolve().parent),
                    interview_context(), prism_context(event),
                ]),
            }
        },
        sys.stdout,
        ensure_ascii=False,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
