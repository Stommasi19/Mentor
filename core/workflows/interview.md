# Mentor interview

Run this full workflow only when explicitly invoked. Ordinary clarification stays
available without it. Follow the shared code policy and relevant project context.
The primary agent handles every stage: do not offer, spawn, or delegate to
subagents, including through a target skill. An interview does not authorize
implementation or change manual preferences.

## Setup: request, target, and local record

Capture the original request, target skill or direct execution, scope, and any
time box verbatim. Requirements-only is a valid target. Ask for a target only
when it is missing; do not ask again about an already stated next action. Check
that a named target is available and can run with the primary agent alone.
Report an unavailable/incompatible target and resolve its replacement with the
user rather than silently choosing one.

Read relevant project references and reuse decisions, acceptance criteria, and
ownership agreements already supplied. Obtain the effective manual level and
coaching state through the adapter's controls contract, carrying the conversation's
session object rather than replacing overrides with saved defaults. Status is
read-only; interview invocation must not save or change preferences.

Use the adapter's artifact helper to reserve a new task directory under
`<data-root>/projects/<project-id>/plans/<date>-<task-slug>/`. Use its returned
location, including any collision suffix, throughout. Report that location and
append the original request, target, constraints, settled answers, and current
teaching/ownership choices to `interview.md` before questions begin. Append each
question table as it is asked and the user's actual answers when received.
Keep these records outside public Git by default. Do not substitute a private
toolkit, background learner ledger, or a different data root after a failure.

## Round 1: high-level decisions

Ask the highest-impact unresolved questions about scope, behavior, constraints,
integration, and verification first. Use a numbered table:

| # | Theme | Question | Concrete options, when useful |
| --- | --- | --- | --- |

Usually 2–5 focused questions suffice; ask fewer when less is missing. Briefly
explain why a decision matters and what its options imply. Let answers shape
later questions rather than asking everything at once. Use examples grounded in
the task, not a compulsory quiz or coding assignment.

## Round 2: teaching and participation

Replace delegation planning with how the primary agent will support this task.
Record known preferences without asking again. Ask only about unresolved choices,
such as a worked example, direct help, or reviewing the approach together.

- Junior: frame requirements with code-flow examples, safe changes and introductory
  component responsibilities.
- Mid-level: invite an approach and examine connected design, contracts, failure
  paths and verification of the complete feature.
- Senior: examine assumptions, alternatives, actual constraints, change risks and
  how decisions will be communicated; deepen explanations on request.

All levels settle the same essential requirements. Coaching intensity and code
ownership are separate. Honor direct implementation/demonstration agreements at
any level; subsequent execution follows the project's contribution expectations.
When coaching is paused, preserve the interview's requirements stages, artifacts,
and confirmation with direct clarification, without teaching prompts or requiring
coaching to resume. Never grade proficiency or infer/switch levels.

## Round 3 and further: drill down

Build on prior answers to resolve meaningful edge cases, failure behavior,
acceptance criteria, and relevant checks. Explain a tradeoff or give a concrete
example when it helps the actual decision. Substantial interviews retain this
three-stage rhythm. Settled small tasks and skip/shorten requests collapse it:
record what is already known, state reasonable assumptions, and move to a concrete
summary without inventing rounds or questions.

## Concrete summary and confirmation

Present task understanding, approach steps, the primary-agent teaching/participation
plan, scope boundaries including the time box, and observable acceptance criteria.
Identify what the rounds resolved, remaining assumptions, and blockers. Say
`Remaining ambiguities: none` only when no blocking decision remains; do not claim
every possible uncertainty is gone. Append this summary to the interview record.

Obtain confirmation of this concrete plan before execution. An existing explicit
approval of that same plan satisfies the gate; initial permission to implement
does not approve a plan with newly chosen requirements. A skip request shortens
questions, not the confirmation gate. If confirmation is needed, finish the turn
with the concrete plan and confirmation question, explaining that this invoked
workflow requires it. Do not use a tool restricted to optional questions to obtain
required approval. Wait for the answer; silence is not confirmation.

## Finalize and continue

After confirmation, complete `interview.md` with the original request, target,
verbatim constraints, questions/actual answers, summary, assumptions, checks, and
confirmation. Write `plan.md` with task understanding, approach, teaching plan,
scope, acceptance criteria, assumptions, and a pointer to `interview.md`. Read both
artifacts back to verify accuracy. Use the helper's successful result as evidence
of persistence; a failed or partial write is not a saved plan. Report the failure,
inspect partial files, and resolve it before execution/handoff. Never claim a
saved artifact that does not exist.

For requirements-only, finish with the confirmed summary and both artifact paths,
leaving implementation untouched. For direct execution, begin the confirmed work
already authorized and run its relevant checks. For an available target, explicitly
invoke that skill with the original request, verbatim constraints, and both artifact
references; read its entrypoint and follow it if the host has no invocation tool.
The primary agent continues to handle the work. Do not silently switch a missing
target to direct execution, add a second blanket approval gate, widen scope, or
treat a planning-only request as permission to implement.

Hand back the artifact locations, selected next action, important choices,
remaining assumptions, and performed/pending checks. Distinguish runtime delivery,
scripted conduct, code correctness/readability, and observed human learning.
