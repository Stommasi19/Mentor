# Mentor

An always-on coding-agent plugin that helps junior developers write
understandable software and practice engineering decisions, implementation,
debugging, and code review.

## Project status

Planning stage. The design and evaluation approach are documented; the plugin,
hooks, supporting skills, and test harness have not been implemented. There is
no installable release yet.

## Intended experience

A lifecycle hook establishes mentoring as the default for coding tasks. The
agent invites the learner to reason through meaningful decisions, prepares
focused coding contributions, and provides hints and feedback. The learner can
ask for a demonstration or have the agent take over a part.

The mentor writes readable code and useful documentation, treats mistakes as
opportunities to investigate, and teaches reviews grounded in actual behavior.
Optional polish stays optional; real defects and required checks remain explicit.

## Mentoring levels

- **Guided:** Step-by-step scaffolding and focused contributions.
- **Supported:** The learner proposes an approach and owns more of the work.
- **Independent:** The learner leads; the mentor mainly reviews and answers questions.

Support fades as the learner consistently demonstrates independent reasoning,
implementation, prediction, and debugging. Levels adapt by concept, remain under
the learner's control, and leave room to attempt, investigate, and revise before
receiving a complete solution.

## First version

- Codex plugin with a shared mentor policy and session lifecycle hook.
- Guided, supported, and independent levels with adaptive help and manual overrides.
- Learning-focused adaptations of `withInterview` and `review` from the
  agentic-workflow toolkit.
- Small C# examples for exercising decisions, coding attempts, and reviews.
- A disposable evaluation environment with separate mentor, simulated junior,
  and observer roles, plus actual plugin-loading checks.

Synthetic conversations assess mentoring behavior. Independent code checks
assess the resulting software. Human exercises assess learner comprehension.

## Planning

- [Design and scope](docs/DESIGN.md)
- [Levels and adaptive support](docs/DESIGN.md#mentoring-levels-and-adaptive-support)
- [Evaluation environment and methodology](docs/DESIGN.md#test-environment-and-roles)
- [Agent instructions](AGENTS.md)

The next implementation slice is the smallest installable plugin foundation:
package manifest, concise mentor policy, and session hook. Supporting workflows
and the evaluation harness follow in focused changes.
