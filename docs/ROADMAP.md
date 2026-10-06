# Mentor delivery roadmap

Status: Planning confirmed; implementation and evaluation have not started.
Repository: [Stommasi19/Mentor](https://github.com/Stommasi19/Mentor).
Local planning baseline: `main` at `2e422c0035301ab5e9504bff0056d73702c83c40`.
The planning changes are local and uncommitted.

The first usable release follows the [implementation plan](IMPLEMENTATION-PLAN.md).
Each slice includes immediate [verification](TESTING.md); a full evaluation
service is not a prerequisite for everyday use.

## First usable release

| Milestone | Useful result | Immediate evidence |
| --- | --- | --- |
| [M01 — hook and code foundation](handoffs/M01-guided-plugin-foundation.md) | A locally installable policy hook establishes code standards and guided coaching defaults. | Actual delivery outside Mentor, executable resource/output checks, readable C# result, and takeover interaction. |
| [M02 — manual levels and preferences](handoffs/M02-manual-levels-and-preferences.md) | Three manual levels, local per-project preferences, and coaching pause/resume. | Different support/participation at each level, project/worktree identity, persistence, retained code standards, and explicit failure behavior. |
| [M03 — interview coaching](handoffs/M03-interview-coaching.md) | Focused learning-oriented requirements clarification. | Questions respond to reasoning, the next step is sufficiently specified, assumptions remain explicit, and direct-implementation requests are respected. |
| [M04 — review coaching](handoffs/M04-review-coaching.md) | Evidence-backed local-diff review practice. | Known bug reported, optional polish distinct, review-comment practice useful, and code/verification evidence explicit. |

M01 can supply early feedback. M01–M04 together are the first usable version
agreed in the interview. Test each portion immediately and record failures/pending
checks before treating it as complete. Automatic progression is initially absent.

## Later milestones

| Milestone | Useful result | Evidence needed |
| --- | --- | --- |
| M05 — isolated scenario runner | Automate repeated mentor/junior/observer runs and baseline comparison. | Controlled contexts/access, recorded authorship, actual hook evidence, independent code checks, and criterion-specific observations. |
| M06 — adaptive support | Gradual concept-specific help changes from a local evidence ledger. | Independent versus assisted reasoning, self-correction, transparent adjustments, manual locks, privacy/reset, and preserved overrides. |
| M07 — human pilot and release preparation | People try related tasks and a supported local package gets a reproducible demo. | Unaided explanation/diagnosis, feedback separate from synthetic results, attribution, and honest installation/support limits. Publication is separately authorized. |

Harder-task selection and other host adapters have separate future scope.
Observations from first use can revise these later handoffs; they do not block
the manual version.

## Current next task

M01 is prepared for an implementation request; no implementation has started.
Account for the local planning changes before creating an implementation branch.
Do not discard existing work or infer installation from these documents.

## Working loop

1. Read the active handoff and applicable criteria; inspect the current baseline.
2. Implement one coherent behavior with relevant checks and documentation.
3. Immediately run the slice's executable, interaction, and required host checks.
4. Review the actual diff; explain an important flow, decision, and failure case.
   Invite coding/review practice according to preferences and project agreements.
5. Record runtime/code/readability/conduct/comprehension evidence separately.
   Unperformed checks stay pending.
6. Update status after verification and prepare the next small change.

Mistakes and failed runs guide revisions. Optional polish and learning gaps do
not become invented shipping defects or perfection gates.
