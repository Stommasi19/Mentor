# M03 — learning-focused interview coaching

Status: Implemented and locally verified on 2026-10-06 for the recorded combination.
Evidence: [M03 results and limitations](../evidence/M03.md).
Usage: [local interview invocation](../../adapters/codex/README.md#interview-coaching).
Dependency: [M02 controls](M02-manual-levels-and-preferences.md).
Scope: [Skill adaptation](../DESIGN.md#adapt-the-agentic-workflow-skills).
Criteria: [T09, T10, T12](../TESTING.md#criteria), plus affected hook/code checks.

## Before and after

Before: a general mentor policy and manual controls.
After: a neutral interview workflow helps clarify a useful next step
through learner reasoning, relevant questions, and explicit assumptions.

## Implementation

1. Inspect the upstream withInterview source/version and redistribution terms.
   Record attribution/notices for copied adaptations; write original instructions
   from the agreed requirements if copying is not permitted.
2. Add `core/workflows/interview.md`, independent of coding language, model/vendor,
   personal paths, memory services, and private personas. Add a thin local host
   invocation wrapper only if required; package/discover it for others in M08.
3. Start from task, selected level, coaching state, project agreements, and what
   the learner has already said. Ask the highest-value question next; invite a
   learner requirement/prediction or experiment when useful.
4. Stop once the next small implementation step is sufficiently understood.
   Record chosen rules, assumptions, and verification. Do not import mandatory
   three-round interviews, delegation interviews, or claims that all uncertainty
   disappeared. No quotas of concerns, diagrams, or questions.
5. Guided can help frame a requirement; supported invites an approach; independent
   uses concise clarification and permits agent implementation. Paused coaching
   retains necessary task clarification without a compulsory learning exercise.
   Respect demonstration/takeover and agent-implements agreements.
6. Let the core policy recommend deeper coaching when relevant; explicit workflow
   invocation must also work. Keep the always-loaded policy concise.
7. Immediately exercise S02, S03 as relevant, a fully specified small task, and
   a direct-implementation/paused-coaching request. Record requirements and checks.

No full architecture/product skills, automatic mastery tracking, runner, or
publication in this slice. The planning interview used the upstream workflow;
Mentor's originally authored runtime workflow intentionally has different pacing.

## Immediate acceptance

- [x] T10: S02 questions respond to the learner's actual uncertainty/reasoning;
  month boundaries/refund choices become explicit before implementation checks.
- [x] T10: a settled small task proceeds proportionately; unresolved assumptions
  remain visible rather than prompting an endless interview.
- [x] T09: a mistaken idea gets a useful hint/investigation; direct help is honored.
- [x] T10: paused coaching and direct-implementation requests retain essential
  clarification without forcing a coding/learning assignment.
- [x] T12/T13 architecture: core workflow runs in a fresh external workspace without private
  toolkit/memory dependencies; transcript observations cite specific turns.
- [x] Record actual local invocation, attribution, affected hook/policy checks,
  and code checks for any scenario implementation produced.

Judge behavior and useful decisions, not exact wording, rounds, insight boxes, or
message length. Keep source permissions unresolved only if no material is copied;
document the actual adaptation path used before marking the slice complete.

## Handback and learning checkpoint

Explain one requirement the learner helped clarify, the evidence that changed a
choice, the remaining assumption, and how the next step will be verified.
Report actual criteria results, failures/pending checks, and updated usage docs.

Completed handback: the scripted learner chose net spending and an exclusive
next-month boundary after a concrete double-count example, then revised the
visible category-matching assumption before implementation. Null behavior remains
unspecified. S02, paused direct implementation and corrected S03 each passed
11/11 independent code checks; the incorrect S03 sample failed the two expected
boundary checks. Nine adapter/runtime tests passed, and native receipts, delivered
guidance and actual workflow reads establish local invocation. Human learning,
broader compatibility and automatic mid-turn compaction remain pending; the
scripted conversation is not evidence of human comprehension. See the evidence
report for execution failures/recovery and source inspection/original authorship.
M04 review coaching is next.
