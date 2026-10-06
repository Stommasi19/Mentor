# Mentor delivery roadmap

Status: Planning revised; implementation and evaluation have not started.
Repository: [Stommasi19/Mentor](https://github.com/Stommasi19/Mentor).
Current local baseline: `main` at `42bc70c7d66c24ef54592a151c97488bbeb38a76`.

Mentor's core is coding-language- and LLM-agnostic. Codex is the first development
adapter; C# is the first test case. Prove behavior and resulting code locally
before preparing other-user installation or marketplace discovery.

Use the [implementation plan](IMPLEMENTATION-PLAN.md) and immediately run the
applicable [criteria](TESTING.md) for each portion.

## First local usable version

| Milestone | Useful result | Immediate evidence |
| --- | --- | --- |
| [M01 — readable-code core and local hook](handoffs/M01-readable-code-core.md) | Neutral policy produces readable, maintainable, appropriately commented code; a development hook loads it automatically. | Baseline/core experiments, actual code/comments/docs review, behavioral checks, and local hook traces. |
| [M02 — manual levels and preferences](handoffs/M02-manual-levels-and-preferences.md) | Three manual levels, neutral local per-project state, and coaching pause/resume. | Different conduct by level, persistence/project isolation, retained code standards, and failure handling. |
| [M03 — interview coaching](handoffs/M03-interview-coaching.md) | Neutral requirements workflow responds to learner reasoning. | Useful clarification, explicit assumptions, next-step verification, and respected direct-implementation requests. |
| [M04 — review coaching](handoffs/M04-review-coaching.md) | Neutral review workflow examines real changes and teaches useful comments. | Known defect reported, optional polish separate, corrected-code checks, and concrete review reasoning. |

M01 provides early experiments; M01–M04 form the first local usable version.
Test each portion immediately. A marketplace entry, distributable plugin manifest,
and public installation are not completion criteria here. Automatic progression
is initially absent.

## Validate and improve the local product

| Milestone | Useful result | Evidence needed |
| --- | --- | --- |
| M05 — portability and isolated scenarios | Exercise another coding language and models from different providers; automate controlled comparisons where useful. | Language/model/host matrix, actual code quality, isolated actor inputs, authorship, and criterion-specific observations. |
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

M01 is ready for an implementation request; no implementation has started.
The planning baseline was committed as “Planning phase”; these revisions update
that plan. Account for the working tree before an implementation branch.

## Working loop

1. Read the handoff and criteria; implement one coherent local behavior.
2. Immediately run executable/code checks and inspect generated code/comments/docs.
3. Exercise the relevant interaction and development hook; distinguish their evidence.
4. Record failures/pending checks and review learner decisions/understanding.
5. Update status and proceed after the portion's required criteria are satisfied.

Distribution is the final phase. Optional polish and knowledge gaps do not
become invented defects or perfection gates.
