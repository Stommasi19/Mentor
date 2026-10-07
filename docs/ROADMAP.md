# Mentor delivery roadmap

Status: M01 and M02 implemented and locally verified on 2026-10-06; M03 is next.
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
| [M03 — interview coaching](handoffs/M03-interview-coaching.md) | Neutral requirements workflow responds to learner reasoning. | Useful clarification, explicit assumptions, next-step verification, and respected direct-implementation requests. |
| [M04 — review coaching](handoffs/M04-review-coaching.md) | Neutral review workflow examines real changes and teaches useful comments. | Known defect reported, optional polish separate, corrected-code checks, and concrete review reasoning. |

M01's early experiments and local hook verification and M02's controls, preferences,
native lifecycle/refresh and conduct checks are complete for the recorded combination.
See [M02 evidence](evidence/M02.md). M01–M04 form
the first local usable version.
Test each portion immediately. A marketplace entry, distributable plugin manifest,
and public installation are not completion criteria here. Automatic progression
is initially absent.

## Validate and improve the local product

| Milestone | Useful result | Evidence needed |
| --- | --- | --- |
| [M05 — portability, optional tooling and isolated scenarios](handoffs/M05-portability-and-tooling.md) | Broaden language/provider coverage; optionally use Serena to improve agent code navigation; automate controlled comparisons where useful. | Tested combinations, actual semantic tool use/fallback, efficiency and code quality, unchanged mentoring contracts, isolated actor inputs and authorship. |
| M06 — adaptive support | Gradual concept-specific changes from a neutral local evidence ledger. | Independent/assisted reasoning, self-correction, visible adjustments, manual locks, privacy/reset, and preserved overrides. |
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

[M03 — interview coaching](handoffs/M03-interview-coaching.md) is next. M02 passes
its required local scope: session-default controls, project-only persistence,
override retention, failed-save recovery, native startup/resume/manual compaction/
clear, two-session refresh, four S01 conditions and S03 direct help. Its
[evidence](evidence/M02.md) separates conduct simulation, code checks and host delivery.
Automatic mid-turn compaction, broader compatibility and human learning remain
pending. M01's baseline and policy candidates both passed; no new causal quality
comparison is claimed. Distribution remains the final phase.

## Working loop

1. Read the handoff and criteria; implement one coherent local behavior.
2. Immediately run executable/code checks and inspect generated code/comments/docs.
3. Exercise the relevant interaction and development hook; distinguish their evidence.
4. Record failures/pending checks and review learner decisions/understanding.
5. Update status and proceed after the portion's required criteria are satisfied.

Distribution is the final phase. Optional polish and knowledge gaps do not
become invented defects or perfection gates.
