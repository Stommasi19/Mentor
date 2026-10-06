# Mentor

An always-on coding-agent plugin that helps junior developers write
understandable software and practice engineering decisions, implementation,
debugging, and code review.

## Project status

Planning stage. The first-release design, implementation plan, verification
criteria, and four handoffs are documented. The plugin, hooks, supporting skills,
fixtures, and test runner have not been implemented. There is no installable
release yet.

## Intended experience

A lifecycle hook establishes readable-code expectations and mentoring defaults
for coding tasks. Coaching invites meaningful decisions, offers coding or review
practice, and provides hints and feedback. The learner can ask for a demonstration
or have the agent take over a part.

The mentor writes readable code and useful documentation, treats mistakes as
opportunities to investigate, and teaches reviews grounded in actual behavior.
Optional polish stays optional; real defects and required checks remain explicit.
Coaching can be paused while readable-code and documentation expectations remain
active. Hook instructions and review/checks work together; the hook does not
certify the quality of generated code.

## Mentoring levels

- **Guided:** Step-by-step help and an offer of a focused coding contribution.
- **Supported:** Less scaffolding, with a choice of coding or reviewing.
- **Independent:** The agent implements by default; the learner directs decisions
  and reviews the result, with help available on request.

The first usable version has manual levels and local per-project preferences.
More experience can mean delegating more implementation while taking ownership
of decisions and review. Later, support can adapt by concept from independent
reasoning, prediction, debugging, and review evidence. Explicit requests can
change who writes code at any level.

## First version

- Codex plugin with a shared mentor policy and session lifecycle hook.
- Manual guided, supported, and independent levels, local preferences, and a
  coaching pause that retains code standards.
- Learning-focused adaptations of `withInterview` and `review` from the
  agentic-workflow toolkit.
- Small C# examples for exercising decisions, coding attempts, and reviews.
- A small reusable C# fixture with immediate checks for each implemented portion,
  fresh conversations, and actual plugin-loading evidence.

Automatic progression, an evidence ledger, the full actor/observer runner, and
a human pilot follow the usable version.

Synthetic conversations assess mentoring behavior. Independent code checks
assess the resulting software. Human exercises assess learner comprehension.

## Planning

- [Confirmed implementation plan](docs/IMPLEMENTATION-PLAN.md)
- [Verification criteria and reusable scenarios](docs/TESTING.md)
- [Delivery roadmap](docs/ROADMAP.md)
- [Next implementation task: M01 — guided plugin foundation](docs/handoffs/M01-guided-plugin-foundation.md)
- [Design and scope](docs/DESIGN.md)
- [Levels and adaptive support](docs/DESIGN.md#mentoring-levels-and-adaptive-support)
- [Evaluation environment and methodology](docs/DESIGN.md#test-environment-and-roles)
- [Agent instructions](AGENTS.md)

The next implementation slice is the smallest installable plugin foundation:
package manifest, concise mentor policy, session hook, and immediate checks.
Manual controls, interview coaching, and review coaching follow in separate
verified slices. Preparing these documents does not begin implementation.
