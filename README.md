# Mentor

A language- and LLM-agnostic mentoring core for coding agents that helps developers
produce readable, maintainable, appropriately commented code while practicing
decisions, implementation, debugging, and review.

## Project status

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

[M04's revised plan](docs/handoffs/M04-review-coaching.md) specifies an explicitly
invoked review skill for local changes or PRs: prime the learner at the selected
level, pause for their review, then discuss evidence-backed findings and save a
report. It reports findings; fixing and posting require separate requests.
Implementation and verification have not started.

[M06's confirmed plan](docs/handoffs/M06-task-feedback.md) replaces automatic
progression with feedback explicitly invoked for the task at hand. It uses
available evidence immediately and saves a local Markdown report, with reflection
optional afterward. Levels remain manually switched. Implementation and verification
are pending; all three requested planning rewrites are complete.

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

## Mentoring levels

- **Guided:** Step-by-step help and an offer of a focused coding contribution.
- **Supported:** Less scaffolding, with a choice of coding or reviewing.
- **Independent:** Agent implementation by default, with the learner directing
  decisions and reviewing the result.

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
- [Next implementation: M04 invoked review skill](docs/handoffs/M04-review-coaching.md)
- [M06 — invoked task feedback, confirmed plan](docs/handoffs/M06-task-feedback.md)
- [Design](docs/DESIGN.md)
- [Authorship and references](docs/ATTRIBUTION.md)
- [Agent instructions](AGENTS.md)

For local development setup, follow the adapter README and the host's ordinary
hook review/trust flow. No marketplace entry, distributable plugin manifest, or
public installation is included. The test workspace's hook was left disabled.
