# Mentor delivery roadmap

Status: M01/M02 and the original M03 workflow locally verified on 2026-10-06.
Revised M03 is implemented and locally verified on 2026-10-07;
[revised evidence](evidence/M03-revised.md) records native invocation and limits.
M04–M07 now share one [local-product implementation plan](IMPLEMENTATION-PLAN.md#m04m07-execution-plan).
The original approved implementation has [local evidence](evidence/M04-M07.md)
and a [requirement audit](evidence/M04-M07-acceptance.md), including native conduct,
model Serena navigation/comparison and disposable DoughTracker pinned-SDK checks.
Broader compatibility, human learning and distribution remain separate; no universal
conduct or efficiency claim is made. The subsequently requested §7a adapter
addition is recorded in [Prism integration evidence](evidence/PR6-Prism.md).
M04's confirmed decisions
are retained alongside M05 tooling, M06 feedback/self-checks and M07's two real-use cases.
M04's [technical implementation plan](handoffs/M04-review-coaching.md#implementation-plan)
was confirmed on 2026-10-07, adopting the evidence rules from the
[upstream migration assessment](UPSTREAM-MIGRATION.md). See current evidence for implementation limits.
Repository: [Stommasi19/Mentor](https://github.com/Stommasi19/Mentor).
M01 implementation branch: `feat/m01-readable-code-core`, based on planning
revision `6e1efc2`. See [evidence and limitations](evidence/M01.md).

Mentor's core is coding-language- and LLM-agnostic. Codex is the first development
adapter; C# is the first test case. Prove behavior and resulting code locally
before preparing other-user installation or marketplace discovery.

Use the [implementation plan](IMPLEMENTATION-PLAN.md) and immediately run the
applicable [criteria](TESTING.md) for each portion.

## First local usable version

| Milestone | Useful result | Immediate evidence |
| --- | --- | --- |
| [M01 — readable-code core and local hook](handoffs/M01-readable-code-core.md) | Neutral policy produces readable, maintainable, appropriately commented code; a development hook loads it automatically. | Baseline/core experiments, actual code/comments/docs review, behavioral checks, and local hook traces. |
| [M02 — manual levels and preferences](handoffs/M02-manual-levels-and-preferences.md) | Three manual levels and pause/resume default to the session; explicit project changes persist in neutral local state. | Different conduct by level, scope/precedence, persistence/isolation, retained code standards, failure recovery, native lifecycle and two-session refresh. |
| [M03 — invoked interview skill](handoffs/M03-interview-coaching.md) | Explicit native skill follows upstream interview stages with teaching and primary-agent-only execution. | Actual skill invocation, focused rounds, confirmation, artifacts/handoff, manual-level support and scope preservation. |
| [M04 — invoked review skill](handoffs/M04-review-coaching.md) | Explicit local/PR review primes the learner, pauses, then discusses evidence-backed findings and saves a report. | Native invocation, level-specific primers, pause/skip/coaching-off, real defect evidence, optional polish and report-only scope. |

M01's early experiments and local hook verification and M02's controls, preferences,
native lifecycle/refresh and conduct checks are complete for the recorded combination.
See [M02 evidence](evidence/M02.md).
The original M03 workflow's invocation, conduct and code checks are recorded in
[M03 evidence](evidence/M03.md). The revised explicitly invoked teaching skill
has separate [native/conduct/code evidence](evidence/M03-revised.md).
M01–M04 form the first local usable version.
Test each portion immediately. A marketplace entry, distributable plugin manifest,
and public installation are not completion criteria here. Levels remain manually
selected; automatic progression is outside the planned release.

## Combined local product delivery — M04–M07

Implement this [combined plan](IMPLEMENTATION-PLAN.md#m04m07-execution-plan) in one sustained
delivery, checking each component as it lands. Keep the milestone IDs for scope
and evidence; no separate interview or blanket approval is required between them
once implementation is requested. Core behavior supports both creating a project
with active help and understanding an existing project from actual source.

| Milestone | Useful result | Evidence needed |
| --- | --- | --- |
| [M04 — invoked review](handoffs/M04-review-coaching.md) | Review local/PR changes with target clarification, focused checks, learner primer/pause and truthful reports. | Native invocation, snapshots, identified defects/gaps, storage, manual preferences and report-only scope. |
| [M05 — portability and optional tooling](handoffs/M05-portability-and-tooling.md) | Exercise C# and Python with existing OpenAI access; add repository-owned opt-in Serena setup/reuse/fallback. | Tested combinations, real semantic calls/fallback, code quality and bounded comparison metrics. Other providers remain pending; no new paid accounts required. |
| [M06 — feedback and PR understanding](handoffs/M06-task-feedback.md) | Immediate task feedback plus a separate explicit PR self-check, each with local reports. | Actual invocation/retrieval, grounded feedback/questions, hint/skip/stop, truthful assistance records and unchanged preferences. |
| [M07 — creation and understanding trials](IMPLEMENTATION-PLAN.md#10-m07-trial-create-doughtrackers-backend) | Evaluate a backend slice in a disposable DoughTracker copy and explain existing Stafr/Crew Workforce backend behavior. | Inspect actual code/comments/docs/checks and supplied observations, then discard trial implementation. The original project stays unchanged; human participation remains pending until observed. |

Shared report storage and PR access serve the new workflows. Ordinary coding help
and source-grounded explanations require no full skill, diff, PR, quiz or report.
The delivery also changes the manual profiles to Junior (code understanding/safe
changes), Mid-level (feature ownership/design) and Senior (engineering judgment),
with compatibility for existing saved/session levels. Readable code, useful
comments and documentation remain the foundation at every level. New profile and
migration boundary checks pass; native profile generation, lifecycle/control,
settled interview and paused-review checks are recorded in the combined evidence.
M02/M03 evidence covers the legacy implementation.
Unavailable cross-provider checks do not block the local build or M06. Mentor
creation trial uses a disposable DoughTracker copy and retains only evaluation
notes/check results. Generated changes are discarded and the original project
stays unchanged. M08 remains the final distribution phase.

Harder-task selection needs a separate experiment. Additional host adapters are
implemented according to demand; universal host support is not assumed.

## Final phase — distribution

[M08 — package and distribute verified behavior](handoffs/M08-distribution.md)
comes after local behavior, code quality, and portability have evidence.
Only here add plugin manifests, marketplace discovery, other-user installation,
update/removal instructions, release assets, and publication steps. Preserve one
canonical core and document the combinations actually supported. Public release
requires its own explicit instruction.

## Current next task

[Revised M03](handoffs/M03-interview-coaching.md) is implemented and locally verified:
a native, explicitly invoked teaching-focused interview skill with staged questions,
confirmation, artifacts and direct execution or skill handoff.
[Revised evidence](evidence/M03-revised.md) records the tested combination;
[original M03 evidence](evidence/M03.md) remains historical.
Use the [combined M04–M07 plan](IMPLEMENTATION-PLAN.md#m04m07-execution-plan) and
[implementation evidence](evidence/M04-M07.md) for the current remaining checks.
It specifies ordinary core help, shared reports/targets, native review/feedback/PR
self-checks, optional Serena, focused verification and both real-project trials.
Runtime implementation is present. Boundary tests, generated fixture checks and
source trials, native PR review/answer/change conduct and actual model semantic
navigation/comparison are recorded. Original delivery acceptance is complete;
broader compatibility and human learning remain pending. The later requested §7a
integration has separate [adapter/host evidence](evidence/PR6-Prism.md).
Levels remain manually switched through M02. Human trial and compatibility claims
follow actual observations rather than the combined delivery label.
M01/M02 evidence remains tied to its recorded controls/lifecycle scope. Automatic
mid-turn compaction, broader compatibility and human learning remain pending.
Distribution remains the final phase.

## Working loop

1. Read the handoff and criteria; implement one coherent local behavior.
2. Immediately run executable/code checks and inspect generated code/comments/docs.
3. Exercise the relevant interaction and development hook; distinguish their evidence.
4. Record failures/pending checks and review learner decisions/understanding.
5. Update status and proceed after the portion's required criteria are satisfied.

Distribution is the final phase. Optional polish and knowledge gaps do not
become invented defects or perfection gates.
