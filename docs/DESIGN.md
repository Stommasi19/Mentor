# Mentor — learning through software engineering

Status: M01's neutral policy, C# experiment fixture, and Codex development hook
and M02's manual controls/preferences are implemented and locally verified on
2026-10-06. Revised M03's native interview skill is implemented and locally verified
on 2026-10-07; [revised evidence](evidence/M03-revised.md) separates runtime,
scripted conduct, code checks, and pending human-learning evidence. This remains a development integration; public plugin
packaging and M04–M08 are planned. [M01 evidence](evidence/M01.md), [M02 evidence](evidence/M02.md),
[implementation plan](IMPLEMENTATION-PLAN.md), and
[verification criteria](TESTING.md) specify the immediate delivery contracts.
Project home: The standalone Mentor repository. The design began in a
DoughTracker discussion and is maintained here independently.

## Purpose

Mentor has a coding-language- and LLM-agnostic core that helps junior developers
write readable, maintainable, appropriately commented software and practice
engineering decisions, implementation, debugging, and code review. Host adapters
make it an always-on plugin or development integration. Its default includes the learner in meaningful
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
- Write descriptive domain names, traceable control flow, and appropriate
  boundaries using the project's language and idioms. Add comments explaining
  intent, constraints, and non-obvious rules, plus useful public-contract
  documentation. Keep them accurate. Review the generated code itself; teaching
  prose in the conversation does not replace needed comments or documentation.
- Treat incomplete ideas and mistakes as opportunities to investigate. Explain
  which part of the reasoning needs revision and why; avoid grades, shaming, and
  invented praise. Do not require a perfect first attempt.
- Respect explicit user instructions and project agreements. The mentoring
  default does not override an agreement that agents implement a complete change.
  Non-coding requests do not acquire a mandatory mentoring exercise.

## Mentoring levels and task support

Levels describe coaching intensity, not a permanent label or a coding quota.
The first usable version defaults to `guided` and supports manual selection,
local per-project preferences, and coaching pause/resume. Level/pause/resume
requests change only the current session unless project scope is explicit.
Session overrides survive resume/manual compaction; clear starts from saved
project preferences. Status refreshes those preferences while retaining session
overrides and showing both effective and saved values. Project reset clears the
current conversation's overrides to guided/on; other sessions retain their own.
Failed project writes still apply locally with an unsaved warning. These M02
contracts are locally verified for the [recorded combination](evidence/M02.md).
Levels remain manually selected throughout the planned release. The learner can
request more/less help, demonstrate/takeover or different implementation ownership
without changing the stored level. M06's invoked task feedback and optional PR
self-check do not infer or switch levels.

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

### Invoked feedback on the task at hand

[M06's confirmed contract](handoffs/M06-task-feedback.md) provides feedback only
when invoked. Use the current task and available requirements, actual changes,
comments/docs, supplied observations and check results. Give concrete strengths,
improvements and an optional next step immediately; reflection can follow but
is not a prerequisite. Do not silently launch another interview or review skill.

Match the manual level: guided explains examples/reasoning, supported connects
evidence and tradeoffs, independent gives concise observations/actions. Coaching-off
retains direct requested feedback without added reflection prompts. Local help can
respond to uncertainty or a direct request without changing the selected level.

Save a local Markdown report with task/scope, evidence, feedback, checks and
limitations in the neutral project data location, outside public Git by default.
Use a task-specific directory; report failed saves honestly and avoid silent
overwrite. Do not store a full transcript, background evidence ledger or proficiency
profile. Feedback-only does not change code or publish findings.

Agent-authored work and passing checks alone establish no learner comprehension.
Discuss independently supplied reasoning only where observed; identify assistance
and keep missing observations unknown. A mistake does not establish overall ability.
Levels and coaching state change through explicit M02 controls only. Automatic
progression thresholds, learner scoring and background tracking are removed from
the planned release; there is no automatic task-difficulty adjustment.

### Optional PR understanding check

A separate explicitly invoked skill accepts a PR link, reads the real change and
asks useful questions: why the approach was chosen, how an input flows through it,
what happens at a boundary, and what tests prove. Ordinary feedback and review
have no quiz requirement.

Wait for the learner's answers before explanations; offer hints, direct help,
skip and stop. Match scaffolding to the manual level, without altering the expected
behavior or assigning a proficiency grade. Explicitly requesting the self-check
permits its questions while coaching is paused without resuming global coaching.

Discuss answers using actual code/test evidence and save local Markdown with
PR/revision, questions/answers, assistance and uncertain/unattempted areas. Refresh
stale context if the PR changes, or explicitly limit the check to the recorded
revision. Respect valid alternative reasoning, disclose serious defects immediately
and do not edit/post/approve/merge as part of a check. No automatic level switch,
progression threshold or background learner profile. Agent-written code and supplied
explanations alone establish no human understanding; a self-check provides limited
evidence about this inspected change, not mastery.

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
that Mentor's levels or teaching workflows improve learning.

## Adapt the agentic-workflow skills

The existing skills are source material for adaptation, not workflows being
executed by this planning document. Inspect the source and its attribution terms
before copying material into the standalone package.

| Source | Keep | Mentor adaptation |
| --- | --- | --- |
| `withInterview` | Target/setup, focused high-level and drill-down rounds, summary/confirmation, interview/plan artifacts, execution or skill handoff | Explicit native skill invocation only. Follow the sequence closely; replace subagent strategy with primary-agent teaching/participation preferences. Explain choices and examples at the selected manual level, reuse settled answers, honor skip requests, and record assumptions without learner assessment. |
| `review` | Target/context/evidence, relevant concerns, review, saved findings and report | Explicit native skill for local changes or PRs. The primary agent primes the learner at the manual level, pauses for their review, then discusses their observations alongside evidence-backed findings. Report only; no automatic fixes, posting, grades or level changes. |
| `archReview` | Tracing boundaries, dependencies, data flow, and failure propagation | Explore one relevant boundary or failure scenario at a time. Ask the learner to sketch or explain the flow; add a diagram when it helps. Replace mandatory diagram counts, exhaustive matrices, and scores with reasoned choices and checks proportional to the task. |
| `productReview` | Asking who needs the behavior, challenging assumptions, considering scope | Let the learner explain the user need, choose the smallest useful behavior, and propose how to test an assumption. Remove forced feature cuts, concern quotas, arbitrary delivery deadlines, and default growth/scale analysis for small learning tasks. |

The first version should adapt `withInterview` and `review`. M03's revised
interview skill follows the [confirmed staged contract](handoffs/M03-interview-coaching.md):
substantial interviews retain the three-stage rhythm, while settled tasks do not
acquire invented questions. Confirmation approves the concrete plan; execution
then continues work already authorized, with requirements-only requests stopping
at their artifacts. Teaching explains requirements/tradeoffs without quizzes,
grades or inferred level changes. Paused coaching retains clarification and task
artifacts without teaching prompts. M04's [confirmed review contract](handoffs/M04-review-coaching.md)
adds a level-specific primer and learner pause before ordinary findings, followed
by discussion and a local report. Its implementation remains pending. Architecture
and product lenses can follow after the basic workflow is exercised.

## Review feedback

The full M04 review skill starts only when invoked, for local changes or a PR.
Read the actual diff/context and relevant evidence first. Prime the learner with
what changed, intended behavior and useful things to inspect: guided gets a
walkthrough/examples, supported a flow map/prompts, independent a brief checklist.
With coaching on, pause for observations or a request to see findings; silence
is not an attempted review. Direct-findings requests skip the wait, and coaching-off
provides a direct report. Disclose serious defects already identified immediately.

Then discuss the learner's observations alongside the evidence-backed review.
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

Save a local report with target/revision, inspected scope, findings/evidence,
checks, optional refinements and limitations. Refresh affected context if the diff
changes during the pause. Relate discussion to observations the learner actually
supplied without scoring ability or writing a proficiency ledger. Report-only
scope does not edit code or post comments; those require separate requests.
Ordinary defect reporting remains available outside the full skill. A learning
gap does not by itself make a correct product change defective.

## Plugin architecture

Keep the canonical policy, learning workflows, preference schema, and evaluation
criteria independent of coding language, LLM vendor, model name, and host API.
Follow the actual project's conventions; do not impose C#, JavaScript, Python,
or vendor-specific defaults on the learner's work.

Thin adapters map supported host hooks, instruction roles, working directory,
state location, and invocation forms to this shared core. A host's hook schema
and skill wrapper belong in its adapter, not in the canonical policy. Revised M03
and M04 require native explicit skill registration through supported local development
facilities, so the workflows fit the eventual Mentor plugin without depending on
Agentic Workflow's installation. Actual invocation must be verified in that host;
a file-read recipe alone does not establish it. Python may implement development
helpers without restricting the target coding language.

Prove the policy first through controlled generated-code experiments, then verify
automatic delivery through a local development hook. For the initial Codex
adapter, use SessionStart for startup/resume/clear/compact, concise context, and
the host's normal hook review/trust flow. This does not need marketplace discovery
or a distributable plugin manifest. Policy-only experiments establish behavior
observations; actual host traces establish automatic delivery.

[M05](handoffs/M05-portability-and-tooling.md) plans optional Serena MCP tooling
through the host adapter, adapting Agentic Workflow's project activation and
semantic-navigation usage. This improves the agent's available tools without
changing mentoring levels, implementation ownership, mentee work or full-skill
activation. Start with read-only navigation and ordinary host edits; keep memory
and onboarding disabled. Retain ordinary search/read/check tools and a visible
fallback when Serena is absent or unavailable. Compare efficiency and actual code
quality before claiming a benefit. The core stays independent of this integration;
implementation and runtime verification are pending. M05 includes repository-owned
setup/launch helpers, configuration examples and usage documentation under
`adapters/codex/serena/`, with integration checks. Reuse an existing compatible
connection in the same host/session, and offer opt-in setup when one is missing;
do not duplicate registration or silently replace user configuration.

Use a small C# fixture initially. Broaden the same criteria to another language
and models from different providers before making broad compatibility claims.
A language/LLM-neutral design and verified support are different evidence.

Marketplace packaging, discovery, installation for others, cache/update/removal
instructions, and publication are the final milestone, after local behavior,
code quality, and portability checks. The [implementation plan](IMPLEMENTATION-PLAN.md)
defines neutral resource/state contracts and the adapter boundary.

## Evaluation examples

### Test environment and roles

Use the [reusable C# fixture and criteria](TESTING.md) with small tasks and runnable
behavioral checks. Test each implemented portion immediately in disposable copies
outside Mentor and active DoughTracker work. Start with direct/scripted scenarios;
the full runner follows the usable version. Its intended roles are:

- **Mentor:** A fresh coding-agent session receiving the shared core. Begin with
  policy-only behavior experiments, labeled as such; then exercise the development
  adapter's real hook for automatic-loading evidence. Codex is the first host.
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

1. **Local delivery and lifecycle checks:** Verify the development adapter's
   output contract and actual delivery in a fresh session. Exercise resume/compaction, disabled or untrusted
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
- Invoked feedback on a current task: Does the report cite concrete evidence,
  leave levels unchanged and offer an optional next step without requiring reflection?
- An invoked PR understanding check: Are questions grounded in the actual change,
  with explanations after attempts and independent/assisted answers distinguished?
- Correct answers that required hints or were supplied by the agent: Does the
  mentor avoid falsely counting them as independent demonstrations?
- An incorrect attempt repaired independently: Does the mentor recognize the
  learner's investigation without treating the first mistake as a demotion?
- Repeated attempts without a new hypothesis, or a direct request for help: Does
  support increase usefully instead of leaving the learner stuck?
- A new concept and a manually selected level: Does useful help preserve the
  selected level and session/project overrides across resume and compaction?

Measure hook/adapter behavior, code behavior, and observed mentoring behavior
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
