# Mentor delivery roadmap

Status: M01/M02 and the original M03 workflow locally verified on 2026-10-06.
Revised M03 is implemented and locally verified on 2026-10-07;
[revised evidence](evidence/M03-revised.md) records native invocation and limits.
M04/M06 planning rewrites are confirmed; M04 is the next implementation slice.
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
selected; optional feedback/self-checks do not switch them. Automatic progression
is outside the planned release.

## Validate and improve the local product

| Milestone | Useful result | Evidence needed |
| --- | --- | --- |
| [M05 — portability, optional tooling and isolated scenarios](handoffs/M05-portability-and-tooling.md) | Broaden language/provider coverage; include repository-owned optional Serena setup and reuse existing connections; automate controlled comparisons where useful. | Tested combinations, actual semantic tool use/fallback, efficiency and code quality, unchanged mentoring contracts, isolated actor inputs and authorship. |
| [M06 — invoked feedback and PR understanding checks](handoffs/M06-task-feedback.md) | Immediate task feedback, plus a separate invoked PR-link self-check with questions and explanations from actual code/tests; local Markdown reports and manually selected levels. | Real PR retrieval, question/answer evidence, independent/assisted/unattempted distinctions, honest reports and unchanged preferences. |
| M07 — personal real-project trial | Use Mentor in the owner's actual work and refine readability/coaching. | Real diff/comments/docs, necessary checks, unaided explanation/diagnosis, and observed friction. |

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
[M04](handoffs/M04-review-coaching.md) is the next implementation slice.
M03, [M04](handoffs/M04-review-coaching.md) and [M06](handoffs/M06-task-feedback.md)
have confirmed planning rewrites, completed one at a time. M04/M06 implementation
and verification have not started. M06 provides invoked task feedback and a
separate optional PR understanding check rather than automatic progression. Levels
remain manually switched through M02.
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
