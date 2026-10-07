---
name: mentor-interview
description: "Explicitly invoked Mentor teaching interview: clarify a task, confirm its plan, save local artifacts, then execute or hand off within the authorized scope."
---

# Mentor interview for Codex

Use only on explicit user invocation. The primary agent runs this workflow and
any target; do not offer or spawn subagents.

Resolve this skill's real directory (follow a development symlink). Run its
`scripts/context.py` with `--workspace` set to the learner's absolute workspace
and `--session` containing the current M02 session JSON (use `{}` only for a
session with no overrides). If the Mentor hook supplied an absolute data root,
pass that exact value as `--data-root`; otherwise the helper reads `MENTOR_DATA_DIR`
or the ordinary local default. Never discard an existing session override.

Read the canonical policy and interview workflow at the returned paths, then
follow the workflow. The helper returns refreshed effective/saved preferences
and shell-quoted control/artifact commands. Retain the returned session object.
Missing resources or invalid locations fail visibly; resolve the failure before
interviewing or executing. These resources are relative to the Mentor checkout,
not the learner workspace. No personal skill installation is required.

For questions, use an available question tool only when its supported role fits;
otherwise ask in the conversation. Preserve the workflow's numbered question
table in `interview.md`. Concrete-plan confirmation is required: when necessary,
ask for it at the end of the turn and wait for the user's reply. Explain that this
explicitly invoked workflow requires confirmation; do not ask for a second gate
after the confirmed plan is saved.

Use the returned artifact command with:

- `create --task <shell-quoted short task label>` to reserve the directory.
- `append --directory <returned absolute directory>` with Markdown on stdin to
  record the original request, constraints, rounds, actual answers, and summary.
- `finalize --directory <directory> --confirmation <actual confirmation>` with
  the confirmed plan Markdown on stdin. Include a pointer to `interview.md`.

Use a quoted heredoc or a safely written input file so Markdown is not evaluated
by the shell. Check exit status and read both files back before claiming persistence.
A failed finalization can leave partial files: inspect and repair them, then retry
before continuing. Requirements-only leaves implementation untouched. Explicit
target invocation passes the original request, constraints, and both artifact paths;
if no skill tool exists, read the available target's entrypoint and follow it
directly as the primary agent. Resolve unavailable targets with the user.
