# Mentor — learning through software engineering

Status: First-release scope confirmed on 2026-10-06. The plugin has not been
implemented or installed. [Implementation plan](IMPLEMENTATION-PLAN.md) and
[verification criteria](TESTING.md) specify the immediate delivery contracts.
Project home: The standalone Mentor repository. The design began in a
DoughTracker discussion and is maintained here independently.

## Purpose

Mentor is an always-on coding-agent plugin that helps junior developers write
understandable software and practice engineering decisions, implementation,
debugging, and code review. Its default includes the learner in meaningful
decisions and coding or review contributions throughout the work.

Success means the learner can explain an approach, predict behavior, investigate
a failure, and justify a review comment. Shipping a working change and learning
from it are separate outcomes. Neither generated explanations nor passing tests
establish the learner's understanding.

## Code standards and coaching

Mentor has two concerns: readable, maintainable implementation with useful
documentation, and coaching that helps the learner practice. Code standards,
material defect reporting, and necessary verification remain active when coaching
is paused. Native plugin disabling turns off the whole package.

The hook supplies default instructions; code review and project checks assess
the resulting change. Instruction delivery is distinct from code quality.

## Default mentor behavior

- Choose one primary learning concept tied to the actual task. Adjust support
  based on the learner's explanations and attempts rather than assumed ability.
- Invite the learner to describe the problem and predict behavior before showing
  the complete answer. Ask focused questions, give progressively clearer hints,
  and provide a worked explanation when requested or when hints are insufficient.
- Discuss meaningful alternatives and their consequences. Ask for the learner's
  reasoning; help them choose and identify evidence that could change the choice.
- Offer a useful coding or review contribution according to the selected level
  and learner preference. Select by purpose, not a fixed number of lines. Prepare
  surrounding context for an accepted coding part, review the attempt, and verify
  the combined result. A demonstration/takeover request receives direct help;
  unaccepted placeholders do not count as a completed change.
- Write descriptive domain names, traceable control flow, focused methods, and
  comments explaining non-obvious rules. Keep documentation accurate and useful
  for following the changed flow and reproducing verification.
- Treat incomplete ideas and mistakes as opportunities to investigate. Explain
  which part of the reasoning needs revision and why; avoid grades, shaming, and
  invented praise. Do not require a perfect first attempt.
- Respect explicit user instructions and project agreements. The mentoring
  default does not override an agreement that agents implement a complete change.
  Non-coding requests do not acquire a mandatory mentoring exercise.

## Mentoring levels and adaptive support

Levels describe coaching intensity, not a permanent label or a coding quota.
The first usable version defaults to `guided` and supports manual selection,
local per-project preferences, and coaching pause/resume. Automatic adaptation
is later scope. The learner can request more/less help, demonstrate/takeover, or
different implementation ownership without changing the stored level.

| Level | Mentor behavior | Learner responsibility |
| --- | --- | --- |
| `guided` | Explain relevant steps, offer a focused coding part with context, and give progressively useful hints. | Make a decision or prediction and try the accepted coding part; request demonstration/takeover when useful. |
| `supported` | Invite an approach with less scaffolding, offer coding or reviewing, and help with demonstrated gaps. | Choose the contribution, justify the approach, and explain relevant verification. |
| `independent` | Implement by default under learner direction, offer concise decision/review checkpoints, and help on request. | Direct the change, review the diff, justify decisions, and understand verification evidence. |

As experience grows, the learner can delegate more implementation and practice
directing/reviewing agent-written code. Coaching intensity and who types code
remain separate; explicit user instructions and project agreements override
these defaults. Independent reasoning can be demonstrated while reviewing code
the agent wrote.

Readable code, accurate documentation, and necessary verification remain goals
at every level. Reducing help does not increase PR size automatically or require
the learner to tackle multiple unfamiliar concepts at once.

### How help fades — later adaptation

Reduce support gradually, one step at a time, based on repeated independent
demonstrations of reasoning and behavior. Relevant evidence includes explaining
why an approach works, implementing it, predicting a related variation, and
diagnosing a failure. An initially incorrect attempt that the learner investigates
and repairs independently can provide strong evidence of progress.

For a later adaptive prototype, use three successful independent observations across at
least two task variants as a candidate for reducing support. The observations
should collectively include an explanation and a failure diagnosis; they are not
a quota of PRs or lines of code. This is a configurable design heuristic to
evaluate, not a scientifically established threshold or a certificate of mastery.
Hint-assisted work records practice, while copied or agent-authored answers do
not count as independent demonstrations. A learner's independent explanation,
prediction, or evidence-backed review of agent-written code can provide evidence;
reasoning supplied by the agent cannot.

Make automatic changes visible with a short explanation of the observations that
motivated them. Adapt separately by concept: someone may work independently on
HTTP endpoints and still need guided support on concurrency. A single error does
not trigger a global demotion. Add support on the current challenge when repeated
attempts reveal a gap or stop producing useful new information, and honor requests
for help immediately.

First-release preferences store the explicitly selected level and coaching state
per project outside Git; see the [storage/control contract](IMPLEMENTATION-PLAN.md#local-preferences).
The later evidence ledger records concept, task variant, observed behavior,
assistance, outcome, evidence reference, and adjustment reason. Keep it local
and inspectable/resettable. Preserve levels/overrides across exercised resume and
compaction. Automatic task-difficulty changes require a separate design; fading
help does not automatically make the problem harder.

### Productive struggle

Leave room for an attempt, inspection of the result, and a revised hypothesis
before supplying the complete solution. Help the learner use errors as evidence.
After the attempt, consolidate what happened and connect it to the underlying
concept. Escalate from a question to a hint, an example, or a worked explanation
as needed; do not prolong confusion to enforce a struggle quota or withhold help
the learner has requested.

This design draws on problem-solving-before-instruction approaches explored in
[introductory programming research](https://arxiv.org/abs/2411.11227). That small
study reported stronger delayed performance on similar tasks, with no difference
in initial outcomes. It motivates evaluation of this design; it does not establish
that Mentor's levels, thresholds, or adaptive policy improve learning.

## Adapt the agentic-workflow skills

The existing skills are source material for adaptation, not workflows being
executed by this planning document. Inspect the source and its attribution terms
before copying material into the standalone package.

| Source | Keep | Mentor adaptation |
| --- | --- | --- |
| `withInterview` | Clarifying goals, surfacing assumptions, discussing constraints | Ask the learner to propose requirements, identify uncertainty, and choose a useful next experiment. Remove the minimum three rounds, mandatory delegation interview, and claim that all ambiguities must disappear. Stop when the next small step is sufficiently understood; record open assumptions. |
| `review` | Reading the actual diff and surrounding code, checking evidence, locating findings, explaining consequences | Invite the learner to review one relevant flow first. Compare their reasoning with an evidence-backed review, provide hints, and help them write a useful comment. Support local diffs and small changes as well as PRs. Use additional reviewers when they serve a concrete concern. |
| `archReview` | Tracing boundaries, dependencies, data flow, and failure propagation | Explore one relevant boundary or failure scenario at a time. Ask the learner to sketch or explain the flow; add a diagram when it helps. Replace mandatory diagram counts, exhaustive matrices, and scores with reasoned choices and checks proportional to the task. |
| `productReview` | Asking who needs the behavior, challenging assumptions, considering scope | Let the learner explain the user need, choose the smallest useful behavior, and propose how to test an assumption. Remove forced feature cuts, concern quotas, arbitrary delivery deadlines, and default growth/scale analysis for small learning tasks. |

The first version should adapt `withInterview` and `review`. Architecture and
product questions can be used as relevant teaching lenses; separate full skills
can follow after the basic mentor workflow has been exercised.

## Review feedback

Keep correctness and learning feedback distinct:

- **Required corrections:** Actual defects or required verification gaps, with
  location, consequence, and a way to confirm the problem. Disclose serious
  issues immediately; do not conceal them to create a quiz.
- **Learning discussion:** A relevant tradeoff, prediction, or debugging question.
  Begin with the learner's reasoning and guide a small experiment or explanation.
- **Optional improvements:** Clearly labeled refinements with a concrete benefit.
  Style preferences and hypothetical future needs do not become shipping gates.

A coaching conversation can focus on one or two learning topics while the review
still reports every material defect it identifies. Unknown behavior stays unknown
until checked. Do not mark required checks passed when they were not performed.

Finish with brief notes on what the learner explained independently, what they
investigated, and what still needs practice. A learning gap does not by itself
make a correct product change defective.

## Plugin architecture

Package a shared mentor policy, lifecycle hook configuration and handler, and
supporting skills. The hook injects the core policy so the user need not invoke a
skill for each coding task. Supporting skills supply deeper interview and review
procedures when relevant.

For Codex, use a command `SessionStart` hook covering startup, resume, clear, and
compact events. The hook establishes default model instructions; it is not a
deterministic code-quality validator. Keep the injected policy concise, and
preserve explicit changes to mentoring preferences when context is refreshed.
Codex requires the current plugin hook definition to be reviewed and trusted
before it runs. Hook scripts must be available in the execution environment.

Create the first version for Codex, with C# examples. Package the adapted skills
without dependencies on the author's `~/.agentic-workflow` installation, global
memory tools, or private agent personas. Add other host adapters after testing
the first workflow. Publishing is a separate task from creating a local package.

## Evaluation examples

### Test environment and roles

Use the [reusable C# fixture and criteria](TESTING.md) with small tasks and runnable
behavioral checks. Test each implemented portion immediately in disposable copies
outside Mentor and active DoughTracker work. Start with direct/scripted scenarios;
the full runner follows the usable version. Its intended roles are:

- **Mentor:** A fresh Codex session using the installed plugin and its trusted
  hook. Use actual hook delivery for integration runs; manually supplying the
  policy is useful for early prompt experiments but does not test plugin loading.
- **Simulated junior:** An isolated actor receiving the public task, relevant
  code, and mentor messages. Give it concrete prior knowledge, misconceptions,
  partial attempts, and rules for responding to hints. Do not give it the mentor
  policy, grading rubric, reference solution, or private evaluation checks.
- **Observer:** Review the transcript, submitted contributions, final diff, and
  actual check results using the criteria below. Blind the observer to whether the
  run used Mentor where practical. Human-review a sample and disputed findings.

A runner exchanges mentor messages and junior replies, submitting junior replies
as user messages to the mentor session. It records the complete interaction and
which participant authored each contribution. Junior code can be submitted as a
patch for the runner to apply and verify in the disposable fixture.

For quick development experiments, a subagent can play the junior. Start it
without inherited conversation history. Separate agent prompts alone do not
isolate filesystem access: use a text-only actor or enforce a separate workspace
to prevent access to the policy, rubric, or reference answers. A capable model
role-playing a novice is a behavioral test actor, not evidence of novice learning.

Begin with scripted junior replies for repeatable regressions, then add reactive
actors for varied conversations. Do not force the actor to follow an identical
conversation when the mentor's questions differ. Fix the initial misconception
and task while letting subsequent responses depend on the actual interaction.

### What each layer establishes

1. **Package and lifecycle checks:** Verify the hook output contract and actual
   delivery in a fresh session. Exercise resume/compaction, disabled or untrusted
   hooks, and explicit changes to mentoring preferences. A policy-only simulation
   cannot establish these behaviors.
2. **Mentoring behavior checks:** Check that the mentor invites a relevant
   prediction or decision and offers a contribution suited to the selected level,
   responds to the actual mistake, and provides useful hints or a requested
   demonstration. Check observable conduct rather than exact wording, message
   length, or the presence of an insight box.
3. **Code checks:** Run independent behavioral checks against the final fixture.
   A strong mentoring transcript does not excuse incorrect code, and correct
   code does not prove useful mentoring. Inspect readability separately.
4. **Human learning checks:** Have people try the workflow, then explain the
   concept or diagnose a related variation without the generated answer. Record
   observations separately from synthetic results; use later recall checks when
   practical. A small pilot provides feedback, not a causal learning claim.

Start with three scenarios: an ambiguous requirement, an incorrect coding
attempt, and a review containing a real bug plus optional polish. Develop the
rubric from these runs before expanding to more scenarios. Retain fresh scenarios
for later evaluation rather than tuning every prompt against the entire set.

### Comparison and evidence

Use the same recorded model, settings, and tasks for baseline and Mentor runs.
Start each condition from identical fixture contents and fresh conversation
context. The baseline excludes Mentor's hook and instructions, including any
project instructions that duplicate its policy. Keep unrelated plugins and
configuration identical. Record repeated runs where practical; preserve observed
failures as useful evaluation evidence.

Use a bounded interaction budget per scenario and record whether a run completed,
needed takeover, failed a code check, or failed a mentoring criterion. Mark
unsupported judgments as inconclusive. Save transcripts, versions/configuration,
hook delivery evidence, diffs, check results, and criterion-specific observations
with cited transcript turns. Do not let an aggregate score hide a real defect.

The remaining scenario ideas are:

- An underspecified task: Does the mentor elicit the learner's reasoning and
  identify a useful next step without an unnecessary interview marathon?
- A design choice with multiple valid answers: Does it explain consequences and
  respond to the learner's reasoning?
- A focused coding contribution: Does it prepare enough context, avoid supplying
  the answer prematurely, give useful feedback, and verify the combined change?
- A mistaken prediction or implementation: Does it guide investigation and revise
  the explanation without treating the mistake as failure of the learner?
- A review containing a real bug and optional polish: Does it report the bug,
  teach an evidence-backed review comment, and keep polish optional?
- A request to take over or a project requiring complete agent implementation:
  Does it respect that instruction?
- A resumed or compacted session: Does mentoring context return while preserving
  the learner's explicit preferences?
- Repeated independent success across task variants: Does support fade one step,
  with an evidence-backed explanation of the change?
- Correct answers that required hints or were supplied by the agent: Does the
  mentor avoid falsely counting them as independent demonstrations?
- An incorrect attempt repaired independently: Does the mentor recognize the
  learner's investigation without treating the first mistake as a demotion?
- Repeated attempts without a new hypothesis, or a direct request for help: Does
  support increase usefully instead of leaving the learner stuck?
- A new concept and a manually locked level: Does adaptation remain specific to
  the concept and respect the override across resume and compaction?

Measure hook/package behavior, code behavior, and observed mentoring behavior
separately. Assess learner comprehension using independent explanations,
predictions, and diagnostic attempts by people; model-generated transcripts alone
do not establish improved human learning.

## Sources inspected

- Agentic-workflow sources inspected in the maintainer's installation:
  `withInterview/SKILL.md`, `review/SKILL.md`, `review/reviewer-prompt.md`,
  `review/triage-prompt.md`, `archReview/SKILL.md`, and `productReview/SKILL.md`.
  Record source version, redistribution terms, and attribution before copying;
  author original instructions when needed. No installation path is a runtime
  dependency of Mentor.
- [Anthropic Explanatory plugin](https://github.com/anthropics/claude-code/tree/main/plugins/explanatory-output-style).
- [Anthropic Learning plugin](https://github.com/anthropics/claude-code/tree/main/plugins/learning-output-style).
- [OpenAI plugin packaging and hooks](https://developers.openai.com/plugins/build/plugins).
- [Codex lifecycle hooks](https://learn.chatgpt.com/docs/hooks).
- [OpenAI skill activation](https://developers.openai.com/plugins/concepts/skills).
- [OpenAI guidance on evaluating agent workflows](https://developers.openai.com/api/docs/guides/agent-evals).
- [Productive failure in introductory Python programming](https://arxiv.org/abs/2411.11227).
