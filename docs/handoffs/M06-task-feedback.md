# M06 — invoked task feedback and PR understanding checks

Status: Implemented on 2026-10-07 with [boundary/report/PR-retrieval evidence](../evidence/M06.md).
Native immediate feedback and PR answer/help/report conduct are recorded, including
labeled changed-revision simulation. Revised plan confirmed on 2026-10-06;
optional PR self-check scope added on 2026-10-07.
Dependency: M01/M02 and the revised [M03 interview](M03-interview-coaching.md)
and [M04 review](M04-review-coaching.md), with shared report/target infrastructure.
Delivery: [Combined M04–M07 implementation plan](../IMPLEMENTATION-PLAN.md#m04m07-execution-plan).
M06 implementation does not wait for unavailable M05 provider coverage.
Scope: Current-task feedback and a separate optional PR understanding-check skill,
with local Markdown reports.
Criteria: [T15, T17, T12, T13](../TESTING.md#criteria) and the
[M06 verification matrix](../TESTING.md#m06-verification-matrix).

## Useful result

The user invokes Mentor's feedback skill to discuss the task at hand and receive
a local Markdown report. It uses available task evidence immediately, explains
concrete strengths and improvements, and suggests an optional next step. Reflection
can follow but is not a prerequisite for feedback.

Junior, Mid-level and Senior remain manually selected through M02's control scope,
with legacy-state compatibility in the combined implementation plan. New profiles
and migration are implemented; legacy choices remain compatibility aliases.
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
4. **Match the selected support.** Junior explains code behavior and safe changes;
   Mid-level connects design/contracts, failure paths and verification; Senior
   examines assumptions, alternatives and consequences. Each retains readable-code,
   useful-comment and documentation expectations and deeper help on request.
   Coaching-off retains directly requested feedback
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

## Optional PR understanding-check skill

The learner explicitly invokes a separate skill with a PR link to check their
understanding of that change. Proposed local name: `mentor-pr-check`; the actual
host invocation is documented and verified during implementation. Ordinary
feedback remains immediate and does not require answering this quiz.

1. **Resolve and read the PR.** The first adapter supports GitHub PR links. Read
   the actual diff, relevant surrounding code, description, tests and documentation;
   record the PR URL, base/head revision and inspected scope. A description alone
   is insufficient. Report missing access, invalid links or unavailable context
   and resolve them before inventing questions. Keep provider APIs in the adapter.
2. **Prepare focused questions.** Derive a small set of useful questions from the
   inspected change: explain its purpose and design choices, trace a real input
   through the changed behavior, predict an edge case or failure, and explain what
   a relevant test establishes or leaves untested. Select what matters to this PR;
   no trivia, fixed question quota or exhaustive exam. Prepare evidence-backed
   answer guidance that allows valid alternative reasoning.
3. **Ask and wait.** Present questions progressively and wait for the learner's
   answers before revealing explanations. Junior asks about real code flow and safe
   changes with context/examples; Mid-level asks about contracts, design and failure
   paths; Senior asks about assumptions, tradeoffs and change risks relevant to the PR.
   Keep the actual answer out of the initial prompt. Hints, direct explanations,
   skip and stop are available immediately on request; unanswered questions are
   marked unattempted rather than treated as a demonstrated misunderstanding.
   Explicit invocation requests this self-check even if coaching is paused, without
   changing the saved/effective coaching state or adding unrelated teaching prompts.
4. **Discuss understanding.** Compare the answer with the actual implementation
   and requirements. Explain supported reasoning, specific gaps and corrections
   with code/test references; accept equivalent valid explanations. Distinguish
   an independent answer from one given after hints or an explanation. Offer an
   optional follow-up prediction after feedback when useful. Do not infer general
   ability, score proficiency, automatically switch levels or guarantee mastery.
   Disclose serious code defects immediately; do not hide them as quiz questions.
5. **Save the self-check.** Write a local Markdown report with PR/revision/scope,
   questions, supplied answers, assistance, code-backed explanations, demonstrated
   reasoning and uncertain/unattempted areas. Keep it in a task-specific directory
   outside public Git, with the same collision/write-failure guarantees as feedback.
   No background learner ledger, full unrelated transcript or automatic progression.
   If the PR changes mid-check, refresh affected evidence/questions or clearly
   finish against the recorded revision; do not use stale answers as current proof.
6. **Finish at learning feedback.** Offer a concrete optional next step. Do not
   edit code, post comments, approve/merge a PR or start fixing because a self-check
   was invoked. The check covers understanding of the inspected change and is not
   a substitute for a correctness review or independent software verification.

Future implementation adds a neutral `core/workflows/pr-understanding.md` and a
thin explicit-only native host wrapper. Reuse M02 preferences and neutral report
handling. Verify real host invocation and PR retrieval separately from scripted
question/answer behavior. A scripted actor's answers do not establish human learning.

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
   and saved defaults. Reuse `runtime/reports.py` and `adapters/codex/reports.py`
   for neutral report handling, plus M04's adapter-owned PR access for the self-check.
   Add no evidence ledger or preference mutations.
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

## Additional acceptance for the PR self-check

- [ ] A supplied GitHub PR link triggers the explicitly invoked native skill and
  actual diff/context retrieval. Invalid/inaccessible targets have visible handling;
  ordinary tasks and feedback do not launch a quiz.
- [ ] Questions have specific code/test evidence and useful reasoning coverage.
  Answers/explanations wait for an attempt or a direct-help request; all three manual
  support styles, coaching-paused invocation, hint/skip/stop and valid alternative
  answers follow the contract without preference changes or grading ability.
- [ ] Known correct and mistaken responses receive supported feedback; unattempted
  and assisted answers stay distinct. Serious defects are disclosed immediately.
  No agent-authored answer is recorded as independent learner reasoning.
- [ ] Markdown records questions/answers, assistance, revision/scope and limitations.
  Changed PRs, unavailable evidence, report collisions and failed saves are handled
  accurately; no whole-project mastery, approval or human-learning claim is invented.
- [ ] Self-check-only leaves code and PR state untouched. Native tool delivery,
  simulated conduct, software checks and observed human comprehension are separate.

## Handback

Give concise task feedback, the local Markdown report location, relevant evidence,
optional next action and pending checks. Do not turn the report into a learner grade
or an automatic recommendation to change mentoring level.
