# M01 — hook and readable-code foundation

Status: Ready for an implementation request; implementation has not started.
Scope: [First usable release](../IMPLEMENTATION-PLAN.md).
Criteria: [T01–T05 and T12](../TESTING.md#criteria).
Local baseline: `main` at `2e422c0035301ab5e9504bff0056d73702c83c40`.
Account for local planning changes before creating the implementation branch.

Inspected tools: Codex CLI `0.160.1`, Python `3.14.3`, .NET SDK `9.0.304`.
Recheck the actual environment during implementation; record tested versions.
Use Python's standard library for helpers and focused contract checks.

## Before and after

Before: planning documents only.
After: an installable local plugin automatically supplies readable-code policy
and guided coaching defaults through a trusted session hook. A disposable C#
interaction demonstrates actual delivery, conditional learner participation,
and a complete checked result after a takeover request.

## Implementation

1. Add `plugins/mentor/plugin.json` using the portable manifest and OpenAI hook
   extension. Add repo marketplace `.agents/plugins/marketplace.json`, named
   `mentor-dev`, exposing source `./plugins/mentor` with required schema fields.
2. Write original `policy/core.md` from the agreed design. Separate code standards
   from coaching: descriptive names, traceable flow, sensible boundaries, useful
   documentation, proportionate questions/hints, and complete verified work.
   Respect explicit requests and project agreements. A learner coding part is
   an offer, not a line quota or required incomplete placeholder.
3. Add `hooks/hooks.json` and `hooks/session_start.py`. Handle startup/resume/clear/
   compact, resolve installed resources independently of working directory, and
   emit supported SessionStart JSON with concise context. Quote plugin paths.
   Missing canonical policy fails with a visible error/nonzero exit. Defaults
   yield to existing explicit session choices.
4. Add the minimal [expense-summary fixture](../TESTING.md#reusable-fixture),
   public S01 task, runnable independent behavior checks, and response cards.
   Copy it outside Mentor for runtime runs. Do not build the standalone runner.
5. Add executable output/resource-failure checks and immediately exercise the
   real handler, actual plugin runtime, and S01 interaction. Document installation,
   trust, installed-cache refresh, and removal using current supported commands.

The policy honors a session request to pause teaching while retaining code
standards; persistent levels/coaching controls are M02. Adapted interview/review
skills, evidence history, automatic progression, MCP services, other hosts,
and publication are excluded from this slice.

## Immediate acceptance

- [ ] T01: marketplace discovery/install and actual trusted hook delivery in a
  fresh external workspace. Record installed path/version and host evidence;
  confirm disabled/untrusted Mentor supplies no policy context.
- [ ] T02: real hook entry point emits valid nonempty event context from another
  directory; missing policy fails visibly. No exact-prose snapshots.
- [ ] T03: record actual startup and exercised resume/clear/compact observations.
  Leave each unexercised lifecycle event pending.
- [ ] T04: inspect S01 final diff for readability and accurate documentation;
  run its independent C# behavior checks and record the actual command.
- [ ] T05: guided offers a useful decision/coding opportunity; accepted work
  receives feedback; demonstration/takeover results in complete verified code.
  Also respect an explicit agent-implements project agreement.
- [ ] T12: keep runtime, code, readability, interaction, and comprehension claims
  separate; no human-learning claim from a simulated actor.
- [ ] README describes only implemented behavior and observed support limits.

Run `python3 -m unittest discover -s tests -v` once checks exist, plus
`git diff --check`. Inspect `codex plugin --help` and subcommand help for actual
install commands. Use the supported hook review/trust flow; no silent trust edits.
Shell-only hook output or manually pasted policy is not runtime delivery proof.

## Handback and learning checkpoint

Report changed behavior/files, actual checks/results, installed/runtime evidence,
failures, pending criteria, and a concise PR description. Explain the path from
marketplace to installed package to trusted hook to model context, and diagnose
an installed plugin whose context is absent. Invite learner understanding and
contributions while honoring their chosen ownership mode.

References: [Design](../DESIGN.md),
[official packaging](https://developers.openai.com/plugins/build/plugins),
[official hooks](https://learn.chatgpt.com/docs/hooks).
Full workflow adaptation and source-attribution checks belong to M03/M04.
