# Mentor agent instructions

Use `README.md`, `docs/ROADMAP.md`, and the active handoff under `docs/handoffs/`
for current scope and status. Use `docs/IMPLEMENTATION-PLAN.md` for first-release
contracts, `docs/TESTING.md` for immediate verification criteria, and
`docs/DESIGN.md` for the intended experience. Read only relevant references.
A previous conversation is not required.

Mentor is a standalone project. DoughTracker can inform examples, but do not
modify its implementation as part of Mentor work. Planning does not itself
authorize implementation.

For implementation requests, agree on a focused slice with observable behavior
and relevant verification. Write readable implementation, tests when they protect
a meaningful contract, and documentation. Explain important decisions and invite
learner participation; respect requests for the agent to implement or demonstrate
a part. Do not impose a fixed coding quota or confuse unfinished placeholders
with a completed change.

Adapt upstream skills for learning: focused questions, explicit assumptions,
progressive hints, meaningful contributions, and evidence-backed review feedback.
Keep optional polish distinct from actual defects. Do not impose exhaustive
interviews, mandatory diagram counts, or perfection scores on small tasks.

Support guided, supported, and independent mentoring levels as specified in the
design. Guided offers a meaningful coding contribution; supported offers coding
or reviewing; independent defaults to agent implementation with the learner
directing and reviewing. Explicit requests/project agreements can change that
allocation. Coaching intensity and who writes code are separate.

Levels remain manually selected, with local per-project preferences. Pausing
coaching retains readable-code/documentation expectations and necessary checks.
The full interview, review, task-feedback and optional PR self-check skills run
only when explicitly invoked, with the primary agent handling their workflows.
Ordinary clarification, help and material-defect reporting remain available
without those skills. M06 provides immediate current-task feedback and a local
Markdown report; reflection is optional and feedback has no quiz prerequisite.
The separate PR self-check grounds questions in actual code/test evidence, waits
for answers and honors hints, explanations, skip and stop. Do not infer/switch
levels, collect a background learner ledger or grade proficiency. Respect overrides
and allow attempts/self-correction. A single mistake does not establish overall
ability. Agent-written code alone establishes no learning; independently supplied
learner reasoning can provide limited evidence on the inspected task.

Implement and verify each requested slice immediately against its handoff and
the applicable criteria. Keep the full evaluation runner outside the critical
path to first use. Report pending checks honestly; policy injection alone cannot
guarantee code readability.

Keep the core independent of any coding language, model, or provider. Host hook schemas,
roles, environment variables, and skill wrappers belong in thin adapters. C# is
an initial test case; Python is a possible helper implementation; neither sets
the learner's coding language. Codex is the first development adapter, not the
core's LLM requirement.

Prove generated-code behavior, readability, useful comments, and documentation
before distribution work. Use local development hooks for early integration.
Marketplace discovery, distributable packaging, public installation, and release
are the final phase. Record tested language/model/host combinations and avoid
claiming universal compatibility from a neutral design alone.

Keep the core/adapters independent of personal toolkit paths and private integrations.
Record upstream attribution when adapting source material. Verify hook delivery
through the actual development host runtime; manually supplied policy tests core
behavior but does not prove automatic hook delivery. Report simulated behavior, code correctness, and observed human
learning separately. Never claim checks or learning outcomes without evidence.
