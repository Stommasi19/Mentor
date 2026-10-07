# M06 — explicitly invoked feedback on the current task

Status: Revised plan confirmed on 2026-10-06; implementation and verification
have not started.
Dependency: M01/M02 and the revised [M03 interview](M03-interview-coaching.md)
and [M04 review](M04-review-coaching.md). Follows M05 in the delivery roadmap.
Scope: Current-task feedback with a local Markdown report.
Criteria: [T15, T12, T13](../TESTING.md#criteria) and the
[M06 verification matrix](../TESTING.md#m06-verification-matrix).

## Useful result

The user invokes Mentor's feedback skill to discuss the task at hand and receive
a local Markdown report. It uses available task evidence immediately, explains
concrete strengths and improvements, and suggests an optional next step. Reflection
can follow but is not a prerequisite for feedback.

Guided, supported and independent remain manually selected through M02's controls.
Feedback does not infer or switch a level, write mentoring preferences or track
progress in the background. It replaces the earlier automatic-progression plan.
The primary agent handles the workflow; no subagents are required or spawned.

## Feedback sequence

1. **Resolve the current task.** Reuse the task and scope already in the conversation.
   Ask only when the task is genuinely ambiguous; do not make the user select a
   different task. Feedback may cover work in progress and must label pending work.
2. **Read available evidence.** Inspect relevant task requirements, actual changes,
   comments/documentation, supplied decisions or observations, and check results
   appropriate to the task. Record scope and revision/snapshot references where
   applicable. State missing context or checks instead of inventing observations.
   Do not silently launch a full interview, review skill or comprehension exercise.
3. **Give task feedback.** Explain what worked, concrete improvements and an optional
   next step, with references to actual behavior or evidence. Separate material
   defects, required verification gaps and optional refinements. Do not require a
   learner reflection or perfect answer before reporting. Disclose every material
   defect identified within the inspected scope; do not promise an exhaustive audit.
4. **Match the selected support.** Guided explains examples and reasoning; supported
   connects evidence and tradeoffs with less scaffolding; independent gives concise
   observations and next actions. Coaching-off retains directly requested feedback
   and code/check standards, without added reflection prompts. Invoking feedback
   does not resume coaching or change effective/saved preferences.
5. **Save a local Markdown report.** Use a task-specific report directory under the
   neutral configured data root/project identity, outside public Git by default.
   A report contains task/scope, inspected evidence, concrete strengths, improvements,
   optional next step, performed/pending checks and limitations. Include learner
   observations only when actually supplied; do not persist a full conversation,
   ongoing evidence ledger or proficiency profile. Avoid silent overwrite and
   report persistence failure accurately, without claiming a saved file exists.
6. **Finish or discuss.** Provide the report location and invite optional reflection
   or clarification when coaching is on. Do not edit implementation, run a fixing
   workflow, post findings, assign compulsory practice or expand the task unless
   separately requested. Level advice is available if explicitly asked; level
   changes still require an explicit control request with M02's scope semantics.

## Evidence limits

Correct agent-written code or passed checks establish software behavior, not the
learner's understanding. Feedback may discuss code quality and task decisions
without grading ability. Only independently supplied learner observations support
claims about their reasoning on this task; identify assistance when relevant.
Absent observations remain unknown and do not block useful task feedback.

No proficiency scores, progression thresholds, automatic level changes, background
collection, concept-specific learner profiles or project-wide progress tracking.
Local help can respond to an explicit request or current task uncertainty without
changing the selected level. Manual preferences and implementation ownership remain
separate from feedback content.

## Future implementation

1. Add one originally authored, language/model/host-neutral
   `core/workflows/feedback.md` from this confirmed contract. No private toolkit,
   memory integration, provider-specific rubric or upstream source is required.
2. Add a thin native host skill wrapper using supported local development
   registration. Verify explicit invocation in the actual host; do not assume a
   command spelling or one host's metadata works everywhere. Keep the full workflow
   out of always-loaded policy; ordinary task help remains available there.
3. Read effective level/coaching state through M02, preserving session overrides
   and saved defaults. Reuse neutral artifact handling as appropriate without
   adding an evidence ledger or preference mutations.
4. Exercise current-task feedback in an external workspace, including work in
   progress, agent-authored work and missing learner observations. Inspect the
   actual report and record native invocation, conduct and check evidence separately.

Public packaging/discovery/installation/publication remain M08. Automatic
progression and background assessment are removed from the planned release;
M06 does not implement a full evaluation runner or establish learning improvement.

## Immediate acceptance

- [ ] A registered native skill starts only on explicit invocation and uses the
  current task without private paths/services. Ordinary work creates no feedback
  report, learner ledger or full-skill activation.
- [ ] Feedback is immediate from available evidence; missing learner reflection
  does not trigger a quiz or block the report. Work in progress and unperformed
  checks are accurately marked pending. No evidence is fabricated.
- [ ] All three manually selected levels produce the agreed explanation style.
  Coaching-off gives direct feedback. Effective/saved preferences remain unchanged,
  including differing session overrides; there is no automatic level switch.
- [ ] Actual task evidence supports strengths, improvements and the optional next
  step. Material defects/verification gaps and optional refinements stay separate.
  Agent-authored work or passing tests alone produces no human-learning claim.
- [ ] A local Markdown report records task/scope, evidence, feedback, checks and
  limitations without a full transcript or proficiency profile. Task-directory
  collisions, missing context and failed saves are handled honestly.
- [ ] Feedback-only leaves implementation untouched and does not post findings or
  invoke fixes. Optional reflection and explicit help requests remain available;
  a separate level-change request uses M02's manual control contract.
- [ ] Usage and actual host results are recorded accurately. Pending compatibility,
  runtime checks and human learning stay separate from document verification.

## Handback

Give concise task feedback, the local Markdown report location, relevant evidence,
optional next action and pending checks. Do not turn the report into a learner grade
or an automatic recommendation to change mentoring level.
