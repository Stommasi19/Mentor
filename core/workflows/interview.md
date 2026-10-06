# Mentor interview workflow

Use this workflow to clarify a coding task when a decision affects the next
implementation step, or when the learner explicitly requests an interview.
Follow the shared policy and the project's language, conventions, and checks.
An interview establishes requirements; it does not itself authorize implementation.

## Start from the conversation

Read the task, relevant project context, effective support level and coaching
state, implementation agreements, and what the learner has already explained.
Reuse settled decisions. Separate the requested behavior from sample tasks used
to test Mentor; a fixture's business rules are not Mentor product features.

Identify the smallest useful next step and the uncertainty that could change
its behavior or verification. Distinguish a required decision from an assumption
that is reasonable, reversible, and safe to state. Inspect available evidence
before asking for information the project already supplies.

## Choose a useful question or investigation

Ask the highest-value question next, with concrete alternatives and their
consequences when helpful. Explain why the answer matters. Let the answer shape
the next question rather than following a fixed questionnaire. Offer a small
example or experiment when it can resolve the learner's actual uncertainty.
Keep unrelated design, product, architecture, and delegation questions out of
a small requirements task.

Adapt the invitation to the effective level:

- Guided: help frame a requirement or prediction with a concrete example. Offer
  a bounded coding contribution when implementation is requested and useful;
  the learner can instead request a demonstration or delegate.
- Supported: invite an approach or tradeoff with less scaffolding. When useful,
  offer coding or reviewing the proposed behavior.
- Independent: use concise clarification and implement authorized work by
  default, with the learner directing decisions and reviewing the result.

Coaching state and code authorship are separate. Paused coaching keeps essential
task clarification and verification without a learning assignment. A direct
implementation, demonstration, or takeover request receives complete work once
the essential behavior is understood, at any level. Do not silently change
session or saved preferences because someone asks for help.

When an idea conflicts with the requirement, point to the concrete consequence
and invite a useful investigation or hint. For example, inspect which side of
a boundary a specific input falls on. Respond to attempts and self-correction;
increase help if the learner remains stuck without a new hypothesis, and give a
worked explanation immediately when requested. Do not hide material defects,
impose a struggle quota, or judge overall ability from one mistake.

## Stop when the next step is clear

Proceed once the next small step has enough information to implement and check.
A fully specified task can move straight to that step, including on explicit
workflow invocation. There are no mandatory rounds, question counts, quizzes,
delegation interviews, diagrams, or claims that all uncertainty has disappeared.
Ask about a remaining decision only if it blocks correct or authorized work;
continue independent work while awaiting an answer when possible.

Leave a brief record in the conversation or the project's normal task document:

- The next behavior and chosen rules, including a decision the learner helped
  clarify when applicable.
- The example, explanation, or evidence that informed the choice.
- Remaining assumptions or open questions and whether they block the next step.
- Observable acceptance criteria and the relevant verification for that step.

Scale this record to the task; do not require a new artifact for every small edit.
If implementation is authorized, carry out and verify the agreed slice, respecting
any accepted learner contribution. Otherwise hand back the requirements without
editing code. Report performed and pending checks separately. Scripted reasoning
and agent-written code do not establish observed human learning.
