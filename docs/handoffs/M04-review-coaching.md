# M04 — learning-focused local-diff review

Status: Queued; implementation has not started.
Dependency: [M03 interview](M03-interview-coaching.md) after M01/M02.
Scope: [Review feedback](../DESIGN.md#review-feedback).
Criteria: [T04, T05, T11, T12](../TESTING.md#criteria).

## Before and after

Before: readable-code policy, manual controls, and requirements coaching.
After: a neutral review workflow helps the learner inspect an actual
change, understand defects, and write evidence-backed review comments.

## Implementation

1. Inspect upstream review instructions/version/terms; record required attribution
   for copied adaptations or author original instructions from the requirements.
2. Add `core/workflows/review.md` without coding-language/model/vendor defaults,
   private agents, memory services, required PR metadata, or mandatory reviewer
   counts. Use thin local host wrappers where needed; distribution is M08.
3. Read the actual local diff and relevant surrounding flow. A PR can supply a
   diff but is not required. State what was inspected, checked, and left unknown.
4. Separate required corrections/verification gaps, learning discussion, and
   optional improvements. Report every identified material defect with location,
   consequence, and confirmation evidence. Disclose serious issues immediately;
   never hide them to create a quiz.
5. Invite learner reasoning on one useful flow and help form a concise comment
   about behavior/evidence. Guided offers steps/hints; supported invites findings;
   independent lets the learner direct review while agent implementation remains
   available. Paused coaching produces a direct review without teaching prompts.
6. Keep code quality and learning outcomes separate. Style preferences, hypothetical
   scale, and a learner knowledge gap do not become invented shipping blockers.
7. Immediately exercise S04's known boundary defect and optional polish, run an
   independent reproduction/check, and repeat with coaching paused. Inspect any
   correction and its actual checks before calling it fixed.

Posting comments, creating PRs, implementing unrelated fixes, full specialized
reviewer orchestration, automatic learner judgments, and publication are outside
this handoff. Review findings alone do not prove a correction has shipped.

## Immediate acceptance

- [ ] T11: workflow reads the actual diff/context and reports the known boundary
  defect with a source location and reproducible consequence.
- [ ] T11: optional polish is visibly separate; all identified material defects
  are reported even if coaching focuses on one topic.
- [ ] T11: learner receives useful help writing/justifying a review comment;
  evidence comes from the real flow/check, not a generic maxim.
- [ ] T04/T05: readable corrected code is checked if produced; takeover respected.
  Material findings remain explicit under coaching-off.
- [ ] T12: report actual commands/results, transcript observations, inspected scope,
  limitations, and unperformed checks without inferring comprehension.
- [ ] Local workflow invocation, attribution, and README usage are tested and
  documented; T13 core neutrality and affected hook/level behavior remain correct.

After this slice, M01–M04 can be called the first local usable version only when their
required criteria have actual passing evidence. A full evaluation runner or
human learning-improvement claim is not required for that local-use milestone.

## Handback and learning checkpoint

Report the defect, its evidence, relevant code checks, optional refinement, and
the learner's independently supplied reasoning where observed. Explain why a
review comment follows from behavior rather than preference. Record remaining
criteria and prepare the first real-task trial described in [TESTING.md](../TESTING.md).
