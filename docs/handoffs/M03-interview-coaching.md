# M03 — explicitly invoked teaching-focused interview skill

Status: Revised native skill implemented and locally verified on 2026-10-07.
See [revised evidence](../evidence/M03-revised.md) for the tested combination,
scripted conduct, software checks, recovery, and limitations.
Historical evidence: [original M03 results](../evidence/M03.md); these passes do
not verify the revised skill contract.
Dependency: [M02 controls](M02-manual-levels-and-preferences.md), after M01.
Scope: [Skill adaptation](../DESIGN.md#adapt-the-agentic-workflow-skills).
Criteria: [T10, T12, T13](../TESTING.md#criteria), plus affected delivery and code checks.

## Useful result

The user explicitly invokes Mentor's interview skill to clarify a task before
executing it or handing it to another skill. Its sequence closely follows Agentic
Workflow's `withInterview`, with the primary agent handling every stage and more
emphasis on explaining engineering decisions. The skill belongs to Mentor's
plugin architecture: one neutral workflow and a thin native host skill wrapper,
usable through supported local development registration before public packaging.

Ordinary necessary clarification remains available outside the full skill.
The agent must not automatically start the full interview. Invocation does not
change manual levels, coaching state, or implementation authorization.

## Interview sequence

1. **Identify the task and target.** Capture the original request, selected target
   skill or direct execution, scope and any time box verbatim. Ask for a target
   only when it is missing; requirements-only is a valid task. Read relevant
   project context and reuse requirements and preferences already supplied.
2. **Create the artifact directory.** Use a task-specific directory under the
   configured neutral local data root, with the existing project identity, such
   as `<data-root>/projects/<project-id>/plans/<date>-<task-slug>/`. Avoid collisions
   with earlier interviews. Report its location and append questions and answers
   to `interview.md` throughout the interview. Do not put full transcripts in
   public Git by default or require the author's Agentic Workflow installation.
3. **Round 1: high-level questions.** Identify scope, behavior, constraints,
   integration and verification decisions. Ask the highest-impact questions first
   in a numbered table with theme, question and concrete options where useful.
   Usually ask 2–5 focused questions; fewer are appropriate when less is missing.
   Briefly explain why a decision matters and what its options imply.
4. **Round 2: teaching and participation preferences.** Replace the upstream
   subagent strategy round with how the primary agent will support this task.
   Use the effective manual level and existing ownership agreements; ask only
   about unresolved preferences, such as a worked example or direct help.
   Record already-settled preferences without asking again. Do not offer, spawn
   or hand off work to subagents as part of this interview workflow.
5. **Round 3 and further drill-down.** Build on prior answers to resolve meaningful
   edge cases, failure behavior, acceptance criteria and relevant checks. Use
   concrete examples to help the learner choose requirements or explain a tradeoff.
   Follow the upstream three-stage rhythm for a substantial interview, but do not
   invent questions to fill rounds on a settled small task. Honor requests to
   skip or shorten the interview while preserving a concrete summary and scope.
6. **Summarize and confirm.** Present task understanding, approach steps, the
   primary-agent teaching/participation plan, scope boundaries including any time
   box, and acceptance criteria. State remaining blockers and explicit assumptions.
   Say `Remaining ambiguities: none` only when no blocking decision remains; this
   does not mean all possible uncertainty disappeared. Briefly identify what the
   rounds resolved. Obtain confirmation of this concrete plan before execution;
   an existing explicit approval of that plan satisfies this gate.
7. **Finalize both artifacts.** After confirmation, finish `interview.md` with the
   original request, target, constraints, questions/answers, summary, assumptions
   and confirmation. Write `plan.md` with task understanding, approach, teaching
   plan, scope, acceptance criteria and a pointer to the interview. If persistence
   fails, report it and resolve the artifact failure before handing off; do not
   claim that an unsaved plan exists.
8. **Execute or hand off.** Invoke the selected available skill explicitly, passing
   the original request, captured constraints and artifact references. For direct
   execution, begin the confirmed work already authorized. Requirements-only
   tasks finish with the summary and artifacts. An unavailable target is reported
   honestly; resolve a replacement or direct execution with the user. Do not add
   a second blanket approval gate after confirmation, widen task scope, or treat
   a planning request as authorization to implement.

## Teaching behavior

- **Guided:** Explain why the question matters, offer concrete examples and help
  frame a requirement or compare its consequences.
- **Supported:** Invite an approach or tradeoff, explain consequential choices
  and offer examples when useful, with less scaffolding.
- **Independent:** Use concise decision questions and let the learner direct the
  approach; provide deeper explanation or a demonstration when requested.
- All levels settle the same essential requirements. Teaching supports real task
  decisions; it does not prescribe quizzes, coding exercises, knowledge checkpoints,
  grades, proficiency claims or inferred level changes. Coaching intensity and
  implementation ownership remain separate.
- Paused coaching preserves the requested interview's requirements stages,
  confirmation and artifacts, with direct clarification rather than teaching
  prompts. Do not require coaching to resume or change saved/session preferences.
- Respect direct help, skip requests and existing project agreements. Subsequent
  execution follows the project's implementation ownership and necessary checks.

## Implementation

1. Revise the canonical `core/workflows/interview.md` from this agreed contract.
   Record inspected upstream version and attribution. Keep original wording unless
   copying terms and required notices are verified; closely matching the process
   does not require copying source text or private integrations.
2. Add a thin native skill wrapper in the development host adapter, registering
   it through supported local facilities. Verify explicit-only activation in the
   actual host; do not assume one host's metadata applies to every adapter.
3. Keep always-loaded instructions concise: code standards, manual preferences,
   ordinary clarification and skill discovery. Remove automatic full-interview
   activation. Load the full interview through explicit skill invocation.
4. Obtain effective level/coaching state through M02's contract, retaining session
   overrides and saved defaults separately. Add neutral artifact handling only as
   needed, with paths supplied by the adapter and no private toolkit dependency.
5. Exercise the revised skill in an external workspace through the actual host.
   Inspect any resulting code/comments/docs and record checks, usage and limitations.

Public packaging, marketplace discovery, installation for others and publication
remain M08. Review coaching, automatic assessment/adaptation, a full evaluation
runner and unrelated specialized workflows are outside M03.

## Acceptance for the revised implementation

- [x] A native skill is registered and explicitly invoked in an external development
  workspace without private paths/services. Hook-provided file-read guidance alone
  does not prove native skill invocation. Ordinary tasks do not start the full skill.
- [x] A substantial task follows setup, high-level questions, teaching preferences,
  drill-down, summary/confirmation, artifacts and execution/handoff. No subagents
  are offered or spawned; known answers and time boxes are retained accurately.
- [x] Guided, supported and independent provide the agreed explanation/scaffolding
  under controlled manual settings. Effective and saved preferences stay unchanged,
  including when they differ. No proficiency judgment or compulsory exercise occurs.
- [x] Settled small tasks and explicit skip requests avoid invented rounds/questions.
  Paused coaching retains clarification, confirmation and artifacts without teaching
  prompts or a requirement to resume coaching.
- [x] Confirmed requirements-only tasks leave implementation untouched. Execution
  waits for concrete-plan confirmation; already-authorized work then proceeds
  without a second blanket gate and receives its relevant checks.
- [x] Both artifacts contain the confirmed scope, assumptions and checks. An available
  target skill receives the request, constraints and references. Missing targets,
  artifact failures and directory collisions have visible, accurate handling.
- [x] Usage, attribution, host invocation, conduct and any generated code/comments/docs
  checks are recorded. Historical passes are not relabeled as revised verification;
  unperformed checks and human-learning outcomes remain pending.

## Handback

Provide the confirmed plan and artifact locations, the selected next action,
important choices and remaining assumptions, and performed or pending checks.
Explain consequential decisions without a learner grade. Keep actual host delivery,
simulated conduct, software correctness and observed human learning separate.
