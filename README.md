# Mentor

A language- and LLM-agnostic mentoring core for coding agents that helps developers
produce readable, maintainable, appropriately commented code while practicing
decisions, implementation, debugging, and review.

## Project status

The approved M04–M07 delivery is implemented and locally verified: Junior/Mid-level/Senior profiles, creation and
source-understanding guidance, explicit review/feedback/PR-check skills, shared
reports/snapshots, optional Serena helpers and a Python fixture. The
[implementation evidence](docs/evidence/M04-M07.md) records 26 passing boundary
tests, C# 11/11 and Python behavior checks, actual native skill discovery and
Stafr's 15 focused checks. Selected native workflows, manual compaction, Serena
MCP navigation and the disposable DoughTracker health build/HTTP checks succeeded.
All-profile/paused Python implementation and feedback, a supported scripted coding
contribution, and a named-model native C# candidate now have checked results.
Ordinary help and a deliberate review wait were also observed with installed
Workflow hooks retained, including recorded hook conflicts. Native controls,
clear/two-session refresh, disabled/untrusted delivery, settled interview,
paused review, live PR review and scripted PR answer/change handling are recorded.
Serena model navigation and the matched build comparison also have actual calls
and checked results. [Acceptance audit](docs/evidence/M04-M07-acceptance.md) identifies
the original scope and limits. Human understanding remains unobserved. The
subsequently requested [Prism adapter integration](adapters/codex/prism/README.md)
has [original checks](docs/evidence/PR6-Prism.md) and
[missing-tool setup/dedicated-memory checks](docs/evidence/PR6-MCP-setup.md);
Mentor's default Prism database is separate from Workflow. M08 distribution remains future work.

M01 is implemented and verified locally: a [neutral policy](core/policy.md),
[Codex development hook](adapters/codex/README.md), and
[C# fixture with independent checks](fixtures/expense-summary/README.md).
The [M01 evidence report](docs/evidence/M01.md) records the comparison, actual hook
delivery, code review, and limitations. The baseline already passed; this sample
does not establish a code-quality improvement or human learning.

Verified combination: C#/.NET 9, OpenAI `gpt-6.1-sol`, Codex CLI/app-server 0.160.1,
macOS arm64. Startup, resume, clear, manual compaction, disabled hooks, and changed
untrusted hooks were exercised. Other languages/providers/hosts remain unverified.

M02 is implemented and locally verified: session controls, explicit project
preferences, failure recovery, native lifecycle retention, and two-session refresh.
The [M02 evidence report](docs/evidence/M02.md) records scope and limitations;
the [adapter guide](adapters/codex/README.md) explains natural controls and local setup.

Revised M03 is implemented and locally verified: the explicit-only native
`$mentor-interview` skill follows staged clarification, concrete-plan confirmation,
local interview/plan artifacts, and primary-agent execution or skill handoff.
[Revised M03 evidence](docs/evidence/M03-revised.md) records native invocation,
manual levels, scope, failure recovery, and generated-code checks;
[original M03 evidence](docs/evidence/M03.md) remains historical.
M04 completes the first local usable version. Packaging for others and publication remain final.

The [combined M04–M07 implementation plan](docs/IMPLEMENTATION-PLAN.md#m04m07-execution-plan)
organizes the implemented local work into one delivery. It covers
active help while creating software and explanations of existing source, plus
review, task feedback, PR understanding checks and optional Serena integration.
Trial cases are a disposable DoughTracker backend build and explanations of
Stafr/Crew Workforce's existing backend. Trial code is discarded after evaluation;
DoughTracker stays unchanged. See current evidence for performed and pending checks.

[M04's confirmed implementation plan](docs/handoffs/M04-review-coaching.md#implementation-plan) specifies an explicitly
invoked review skill for local changes or PRs: prime the learner at the selected
level, pause for their review, then discuss evidence-backed findings and save a
report. It reports findings; fixing and posting require separate requests.
An invocation without a target asks what to review. Relevant focused checks run
against the reviewed snapshot; stale evidence and required verification gaps stay
distinct from reproduced defects. The plan adopts the evidence rules from the
[upstream migration assessment](docs/UPSTREAM-MIGRATION.md).
Implementation and selected native conduct checks are recorded in
[M04 evidence](docs/evidence/M04.md), including paused review.

[M06's plan](docs/handoffs/M06-task-feedback.md) provides immediate invoked task
feedback and a separate optional PR understanding check, with local Markdown
reports. Reflection is optional for ordinary feedback; levels remain manually
switched. [M05](docs/handoffs/M05-portability-and-tooling.md) covers opt-in Serena
and C#/Python verification using existing OpenAI access. Other providers stay
unverified/pending, with no new paid model accounts required for this delivery.

Run the adapter checks with `python3 -m unittest discover -s tests -v`.
Use the fixture's `check.py` against a completed disposable candidate; the checked-in
starter is intentionally unfinished and must fail its behavior checks.

## Intended experience

A shared policy establishes code standards and optional coaching. Thin host
adapters load that policy automatically through the host's supported hooks.
Codex is the first development adapter; C# is the first fixture, not a restriction
on the product's coding language or LLM.

The core follows the project's language and conventions. It asks for descriptive
names, understandable flow, appropriate boundaries, comments explaining intent
and non-obvious rules, and useful accurate documentation. Comments must appear
where needed in the resulting code; a verbose chat explanation does not replace
them. Review and behavioral checks assess the actual change.

Coaching invites decisions, offers coding or review practice, and provides hints
and feedback. The learner can request a demonstration or takeover. Pausing
coaching leaves code standards and necessary verification active.
For new work, support a meaningful accepted coding contribution and verify the
complete result. For existing work, inspect actual source and explain responsibilities,
request/data flow, failures and check limits with concrete locations. Ordinary
explanations have no diff/PR, quiz, special walkthrough skill or report prerequisite.

## Mentoring levels

- **Junior:** Code understanding, safe changes, debugging, tests and review, with
  introductory system design and an offer of a focused coding contribution.
- **Mid-level:** Feature ownership, system design, contracts, failure handling,
  refactoring and verification, with a choice of coding or reviewing.
- **Senior:** Engineering judgment, assumptions, architectural tradeoffs,
  reliability, change risks and technical communication. Agent implementation
  defaults to learner direction and review.

These profiles are implemented from the [active implementation plan](docs/IMPLEMENTATION-PLAN.md#manual-mentoring-profiles).
Guided/Supported/Independent remain compatibility aliases; legacy saved/session
choices translate read-only until an explicit project write. Readable code, useful comments and accurate
documentation remain the foundation at every level and with coaching paused.
Help on any topic and explicit coding-ownership overrides remain available.

Choose **manual coding** when you want to write all the code and receive insightful
guidance, progressive hints, explanations and reviews. Mentor leaves project
implementation untouched and avoids complete task solutions unless you explicitly
ask for a demonstration or implementation of that part. It then returns to manual
guidance. This choice is independent of level and stays active when coaching is
paused. **Assisted coding** retains the existing allocation of work.

Say “use manual coding” for this conversation or “save manual coding for this
project” to retain it across conversations. “Use assisted coding” switches back.
Status shows the effective and saved mode. Existing records default to assisted
without a write. This is an agent behavior setting, not a filesystem permission
lock. See the [manual coding handoff](docs/handoffs/manual-coding-mode.md) for
verification and limitations.

The first local version has manual levels and per-project preferences outside
Git. Level/pause/resume requests change the session unless project scope is
explicitly requested. Session overrides survive resume/manual compaction; clear
starts from saved project preferences. Status shows effective and saved choices;
failed saves still apply locally with an unsaved warning. Saved fields are updated
separately, so a temporary session pause cannot become a project default when
changing the saved level. See [storage contracts](runtime/README.md).

Greater experience can mean delegating more code while owning decisions and
review. Task feedback can explain concrete strengths, improvements and an optional
next step; it does not switch levels or track proficiency. Explicit requests can
change implementation ownership at any level.

## Build and prove locally

1. Write the neutral policy and test generated code, comments, and documentation
   against a small C# case and controlled baseline.
2. Verify automatic policy loading with a local development hook.
3. Add manual levels/preferences and invoked interview/review skills; test each
   portion immediately.
4. Broaden language/model coverage, add invoked task feedback, and try real project work.
5. Finally package and document the verified behavior for other users, including
   marketplace discovery and installation.

Synthetic conversations assess conduct. Behavioral checks assess software.
Readability review examines code/comments/docs. Unaided human exercises assess
comprehension. A neutral design is not proof that every model or host is supported;
record the combinations actually tested.

## Project references

- [Implementation plan](docs/IMPLEMENTATION-PLAN.md)
- [Verification criteria and scenarios](docs/TESTING.md)
- [Delivery roadmap](docs/ROADMAP.md)
- [Completed M01 handoff](docs/handoffs/M01-readable-code-core.md)
- [Completed M02 handoff](docs/handoffs/M02-manual-levels-and-preferences.md)
- [M03 — invoked interview skill, locally verified](docs/handoffs/M03-interview-coaching.md)
- [Combined M04–M07 implementation plan](docs/IMPLEMENTATION-PLAN.md#m04m07-execution-plan)
- [M04 — invoked review contract](docs/handoffs/M04-review-coaching.md)
- [M05 — portability and optional tooling](docs/handoffs/M05-portability-and-tooling.md)
- [M06 — task feedback and PR understanding](docs/handoffs/M06-task-feedback.md)
- [Design](docs/DESIGN.md)
- [Authorship and references](docs/ATTRIBUTION.md)
- [Agent instructions](AGENTS.md)

For local development setup, follow the adapter README and the host's ordinary
hook review/trust flow. No marketplace entry, distributable plugin manifest, or
public installation is included. The test workspace's hook was left disabled.
