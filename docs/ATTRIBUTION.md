# Mentor authorship and references

The Mentor core policy, adapter, fixture, and checks were authored for this
project from its agreed design and implementation contracts. M01 does not vendor
or adapt the source text of an upstream mentoring plugin or skill. The design
document retains the project's earlier inspiration references.

The Codex protocol was checked against the installed CLI/app-server 0.160.1 and
the [official hook reference](https://learn.chatgpt.com/docs/hooks).
[Official skill configuration guidance](https://learn.chatgpt.com/docs/build-skills)
informed isolation of the local comparison runs.

OpenAI Docs and testAudit were development-time aids. No personal toolkit path,
memory integration, installed skill, or private service is a dependency of the
policy, adapter, fixture, or checks. Later milestones must record source versions,
licenses, and required notices before copying or adapting upstream source.

M02's neutral controls workflow, preference helper, Codex control entry, and
contract checks were also authored from Mentor's agreed contracts. No upstream
skill source was copied into the runtime or workflow. The official hook reference
informed the bounded extended context configuration; testAudit's authoring gate
was used as a development aid. Neither is a runtime dependency.

M03 inspected `withInterview` from the local Agentic Workflow release
`e0ff305-portable-20261006T031059Z`, whose README identifies
`vitalizecare/agentic-workflow` as its source repository. The inspected
`skills/withInterview/SKILL.md` has SHA-256
`f6cc85807ffb378296cf69c6d9b4c4f3d2aef0a0f59e0fc4a7669f293b6ddf11`.
The installed release has no Git metadata or license/notice granting
redistribution of this skill; its exact upstream commit and copying permissions
are unconfirmed. No upstream text, templates, or code were copied into M03.
Instead, the interview workflow, invocation guidance, and scenario cards were
authored from Mentor's agreed requirements. The upstream's ideas of clarifying
goals, assumptions, and constraints are acknowledged as design inspiration.
Its mandatory rounds, delegation interview, confirmation gate, private paths,
and memory integrations are not runtime dependencies. No copied-source notice
is required for this original implementation; copying upstream material later
still requires verified terms and any required notices.

The confirmed M03 planning revision closely follows the inspected `withInterview`
process: target/setup, focused rounds, summary/confirmation, artifacts and handoff.
It replaces subagent strategy with primary-agent teaching preferences and fits
Mentor's neutral core/thin plugin-adapter design. The plan is written originally;
source redistribution terms remain unconfirmed. The original runtime described
above remains historical. The revised M03 implementation was originally authored
from the confirmed contract, retaining setup, focused rounds, confirmation,
artifacts, and primary-agent execution without copying upstream text/templates.
The same inspected source hash was rechecked on 2026-10-07. Skill Creator and
testAudit served as development aids only. Native discovery, symlink handling and
explicit-only metadata were checked against the installed Codex 0.160.1 protocol
and the [official skill guide](https://learn.chatgpt.com/docs/build-skills).
No author toolkit path, upstream installation, or private service is required.

M04's planning rewrite inspected `skills/review/SKILL.md` in the same Agentic
Workflow release (`e0ff305-portable-20261006T031059Z`), SHA-256
`2b4d61be25e1110b9cd1ccb7f283dfdd161db12152bd7426dbc60391033062f2`. The originally worded plan adapts target/context/evidence, review
and local reporting into a primary-agent workflow with learner priming and a
pause. No upstream source text, code or templates were copied. Redistribution
terms remain unconfirmed; any future copying requires verified terms/notices.
Runtime implementation is now present; [performed checks and pending native evidence](evidence/M04-M07.md) are separate.

The M04 implementation plan confirmed on 2026-10-07 adopts the evidence rules
documented in the [upstream migration assessment](UPSTREAM-MIGRATION.md).
The replacement checkout identifies
`joi-fairshare/agentic-workflow` as its origin and is clean at
`e0ff305a0f17746858bd63e4752047731edf2282`. Local inspection rechecked these
SHA-256 fingerprints on 2026-10-07:

| Source | SHA-256 |
| --- | --- |
| `skills/review/SKILL.md` | `25963b307f21f338e59d1def71ea1db77c2b0e37bbfedc0de00e4a3f864e9946` |
| `skills/review/reviewer-prompt.md` | `8e1ea89797a742fffe13f804e720d92dc1662637fbe01d6cc1b2b0ad4deffaa5` |
| `skills/review/triage-prompt.md` | `82246b09b7c4eb8b208c8ae1d94a00d9587642edf1af65aa068f409684de85e1` |
| `skills/withInterview/SKILL.md` | `f6cc85807ffb378296cf69c6d9b4c4f3d2aef0a0f59e0fc4a7669f293b6ddf11` |

The interview entrypoint matches the historical fingerprint; the review entrypoint
differs. The previous portable source is unavailable for a complete textual delta,
so the cause of the review difference remains unconfirmed. Preserve the historical
records above rather than relabeling them as replacement-source evidence.

No repository-wide LICENSE was found in the tracked replacement files.
`skills/testAudit/NOTICE.md` applies to that skill's adaptation, not permission to
redistribute the review/interview sources. This technical plan was authored from
Mentor's contracts and confirmed answers; no upstream source text, code or templates
were copied into Mentor. The implementation plan calls for original instructions;
any later copying still requires verified applicable terms and notices. Upstream
setup, private services and author toolkit paths are not Mentor dependencies.
Runtime implementation and local checks are recorded in [current evidence](evidence/M04-M07.md);
new native conduct and human-learning evidence remain pending.

The combined M04–M07 technical plan reuses Mentor's own M05/M06 planning contracts
from branch `docs/m05-serena-tooling` at
`86c3ee7ee31e3c099e2f30499593961a9ff545b9`, together with the confirmed M04
contracts and subsequent user clarifications. It specifies ordinary creation and
existing-code assistance, existing OpenAI access, shared reports/PR access and two
real-project trials. These are planning documents, not runtime evidence. No external
skill text/templates or Serena implementation were copied into Mentor. Inspect
actual Serena versions/capabilities and applicable terms during implementation;
private Docker launchers and toolkit setup are not reusable adapter dependencies.

## Implemented M04–M07 resources

The new policy/profiles, review/feedback/PR-understanding instructions, report and
snapshot helpers, wrappers, optional-tool helpers/config and Python fixture were
originally authored from Mentor's approved contracts. No upstream skill text,
Serena implementation or private launcher was copied. Development-time testAudit
and skill-creator were used for authoring checks; neither is a product dependency.

GitHub transport follows the [official gh API reference](https://cli.github.com/manual/gh_api).
Serena setup/configuration was checked against its
[official CLI](https://github.com/oraios/serena/blob/main/src/serena/cli.py),
[context/mode schema](https://github.com/oraios/serena/blob/main/src/serena/config/context_mode.py),
[tool inclusion schema](https://github.com/oraios/serena/blob/main/src/serena/config/serena_config.py)
and [memory disabling guide](https://oraios.github.io/serena/02-usage/045_memories.html)
on 2026-10-07. These references describe API/configuration usage; installed-server
version/acceptance is unverified. Code identifiers and configuration keys do not
represent vendored source. See [actual evidence](evidence/M04-M07.md) for limits.

## PR #6 Prism follow-up

Original adapter request preparation and instructions adapt the session-load,
project-work ledger and versioned handoff pattern inspected in Agentic Workflow's
[`skills/_preamble.md`](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/skills/_preamble.md).
No upstream source text, templates or implementation are copied. Unlike that
upstream workflow, unavailable Prism does not stop ordinary Mentor work, and
project saves require an explicit request. Native tool schemas and installed
`prism-mcp-server@20.21.17` behavior were inspected; actual host calls verify the
recorded subset. Prism itself is not vendored or installed by Mentor. Its
[upstream documentation](https://github.com/dcostenco/prism-coder) describes setup
and transport. Reusing the host connection introduces no private toolkit path,
new paid model account or second registration into Mentor.
