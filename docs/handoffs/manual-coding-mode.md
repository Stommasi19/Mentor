# Manual coding mode

Requested on 2026-10-17 after confirming there was no saved guidance-only control.
Scope: add manual/assisted coding ownership to the existing local preference and
Codex control lifecycle; keep it independent of Junior/Mid-level/Senior and coaching.

## Behavior

- `manual`: learner writes all project implementation. Mentor inspects, explains,
  gives progressive hints and evidence-backed reviews, suggests checks and runs
  requested non-destructive checks. No project implementation edits or complete
  task solutions unless the user explicitly requests that part.
- A feature request or plan confirmation starts guided learner work. An explicit
  request to implement, fix, demonstrate or take over allows that part only;
  manual guidance resumes afterward without changing preferences. Requested
  interview plans and review/feedback reports may still be saved.
- `assisted`: retain the current profile allocation and explicit agreements.
  Existing projects remain assisted until they choose manual mode.
- Session changes write nothing. Explicit project changes save the mode across
  conversations. Pause/resume and level changes preserve ownership. Reset restores
  Junior/on/assisted. Older schema-1/2 records read as assisted without a write;
  explicit project changes write schema 3. No proficiency/learner ledger is added.

## Use

Say “use manual coding” for this session, “save manual coding for this project”
to persist, or “use assisted coding” to switch back. The hook-supplied control
command supports `set-coding-mode manual|assisted`, with `--scope project` only
for an explicit save. `status` shows effective and saved choices.
`--field coding_mode use-project` drops just that session override.

## Verification

Process checks and any native conduct evidence are recorded in
[the evidence report](../evidence/manual-coding-mode.md). Preserve the checkout's
existing uncommitted M04–M07 work. No default is silently enabled in a real learner
project, and no existing saved preferences are migrated during inspection.

This is a persistent Mentor behavior setting, not a host tool-permission sandbox.
Native automatic delivery and model compliance must be observed separately from
preference persistence and handler output; no human-learning result is implied.
