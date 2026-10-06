# Mentor

A language- and LLM-agnostic mentoring core for coding agents that helps developers
produce readable, maintainable, appropriately commented code while practicing
decisions, implementation, debugging, and review.

## Project status

Planning stage. The core, development adapter, fixtures, and executable checks
have not been implemented. The first priority is demonstrating useful behavior
and good generated code locally. Marketplace discovery, packaging for other
users, and publication are the final phase.

## Intended experience

A shared policy establishes code standards and optional coaching. Thin host
adapters load that policy automatically through the host's supported hooks.
Codex is the first development adapter; C# is the first fixture, not a restriction
on the product's coding language or LLM.

The core follows the project's language and conventions. It asks for descriptive
names, understandable flow, appropriate boundaries, comments explaining intent
and non-obvious rules, and useful accurate documentation. Comments must appear
where needed in the resulting code; a verbose chat explanation does not replace
them. Review and behavioral checks assess the actual change.

Coaching invites decisions, offers coding or review practice, and provides hints
and feedback. The learner can request a demonstration or takeover. Pausing
coaching leaves code standards and necessary verification active.

## Mentoring levels

- **Guided:** Step-by-step help and an offer of a focused coding contribution.
- **Supported:** Less scaffolding, with a choice of coding or reviewing.
- **Independent:** Agent implementation by default, with the learner directing
  decisions and reviewing the result.

The first local version has manual levels and per-project preferences outside
Git. Greater experience can mean delegating more code while owning decisions and
review. Later evidence can support concept-specific adaptation. Explicit requests
can change implementation ownership at any level.

## Build and prove locally

1. Write the neutral policy and test generated code, comments, and documentation
   against a small C# case and controlled baseline.
2. Verify automatic policy loading with a local development hook.
3. Add manual levels/preferences, interview coaching, and review coaching; test
   each portion immediately.
4. Broaden language/model coverage, evaluate adaptation, and try real project work.
5. Finally package and document the verified behavior for other users, including
   marketplace discovery and installation.

Synthetic conversations assess conduct. Behavioral checks assess software.
Readability review examines code/comments/docs. Unaided human exercises assess
comprehension. A neutral design is not proof that every model or host is supported;
record the combinations actually tested.

## Planning

- [Implementation plan](docs/IMPLEMENTATION-PLAN.md)
- [Verification criteria and scenarios](docs/TESTING.md)
- [Delivery roadmap](docs/ROADMAP.md)
- [Next task: M01 — readable-code core and local hook](docs/handoffs/M01-readable-code-core.md)
- [Design](docs/DESIGN.md)
- [Agent instructions](AGENTS.md)

The next slice proves the core and local automatic loading. No marketplace entry,
distributable plugin manifest, or public installation is needed for that slice.
