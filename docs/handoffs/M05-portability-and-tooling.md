# M05 — portability, optional Serena tooling and isolated scenarios

Status: Planned; implementation and verification have not started.
Dependency: Local M01–M04 behavior and code-quality evidence.
Scope: Broader coverage plus an optional tool integration for the coding agent.
Criteria: [T13, T16, T12](../TESTING.md#criteria), with existing code-quality,
participation and preference criteria where affected.

## Useful result

Exercise Mentor with another coding language and models from different providers,
then add optional Serena tools to help the agent understand and navigate code more
efficiently. Better tools can support better implementation; they do not determine
what work the mentee receives. Selected mentoring levels, implementation ownership,
teaching, pauses and skill activation retain their agreed contracts.

Mentor remains usable without Serena. Its neutral core has no Serena, LSP, Docker,
host or provider dependency; concrete registration/configuration belongs in adapters.

## Planned slices

### Portability and optional tooling

1. Extend the tested language/model/host matrix using the existing rubric. Record
   actual code behavior, readability, comments/docs and conduct for each combination.
   A neutral design alone does not establish compatibility.
2. Inspect Agentic Workflow's Serena usage at the pinned revision listed below.
   Reuse its useful integration patterns: explicit workspace/project activation,
   language-server configuration, semantic navigation for code structure, and
   ordinary search/read tools for text or complete context. Adapt source only after
   verifying redistribution terms and required notices; otherwise author original
   configuration and guidance. Do not copy its full toolkit installer.
3. Add an opt-in Serena MCP connection through the development host's supported
   configuration. Keep workspace identity, launch/context options and language
   prerequisites in a thin adapter. Start with the upstream's read-only navigation
   pattern; the agent continues editing with the host's ordinary tools. Evaluate
   a Docker wrapper only if useful for the tested environment; it is not a core
   requirement. Verify exact tool names and capabilities against the installed
   Serena version instead of copying stale aliases.
4. Guide the agent to use semantic tools for definitions, references and file
   structure, while retaining `rg`, file reads, diff inspection and real checks
   where appropriate. Optional tooling improves agent capability across coding
   workflows; it does not change learner assignments or silently invoke coaching.
5. Keep Serena memory/onboarding features disabled for this integration. Preserve
   Mentor's preference/artifact ownership; add no background learner tracking.
   An absent, disabled or failing server has a visible fallback to ordinary tools
   without blocking Mentor's policy or falsely claiming semantic checks ran.
6. Exercise actual MCP connection, project activation and symbol/reference calls
   in an external workspace. Include another cwd/worktree, unavailable-server
   fallback and the tested language prerequisites. Record host/Serena/backend
   versions and observed limitations; handler/configuration output is not delivery
   evidence.
7. Compare the same coding task with and without Serena, holding the model,
   preferences, ownership agreement, starter and requirements constant. Measure
   available token usage, tool calls and elapsed time alongside correctness,
   readability and comments/docs. Disclose startup/indexing overhead and unavailable
   metrics. No universal speed or quality improvement is assumed.

### Isolated scenarios

Automate controlled comparisons only where useful, keeping simulated actor inputs,
observer material and private checks isolated. Preserve authorship and assistance
records; simulated conduct and software checks do not establish human learning.
The full evaluation runner remains outside the critical path to first local use.

## Immediate acceptance when implemented

- [ ] Portability results identify the actual language/model/host combinations,
  code-quality evidence and pending coverage.
- [ ] Opt-in Serena works through the real host in an external workspace, with
  correct project activation and observed semantic tool calls. Private toolkit
  paths and global toolkit installation are unnecessary.
- [ ] Mentor works without Serena and recovers visibly when it is unavailable;
  no semantic result or successful activation is fabricated.
- [ ] Definitions/references/file structure use supported semantic tools where
  helpful; text search, full context, edits and checks retain appropriate tools.
- [ ] Tool availability does not switch levels, mutate session/project preferences,
  change implementation ownership, force mentee work or launch a full skill.
  Memory/onboarding and background learner tracking remain disabled.
- [ ] Controlled comparison records efficiency metrics, actual code/comments/docs
  and limitations; unchanged or worse results are reported honestly.
- [ ] Any automated scenarios preserve input isolation and evidence distinctions.
  Source attribution, usage and performed/pending checks match the implementation.

## Source and boundaries

Inspected Agentic Workflow revision:
[`e0ff305a0f17746858bd63e4752047731edf2282`](https://github.com/joi-fairshare/agentic-workflow/tree/e0ff305a0f17746858bd63e4752047731edf2282).
Relevant sources are its
[tool-routing guidance](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/.agents/rules/mcp-servers.md),
[Serena project configuration](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/.serena/project.yml),
and [Docker launcher](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/scripts/serena-docker).
Consult current [Serena client guidance](https://oraios.github.io/serena/02-usage/030_clients.html)
and [language support](https://oraios.github.io/serena/01-about/020_programming-languages.html)
when implementing; recorded versions must match the actual experiment.

This is a planning change: no tools are installed, registered or enabled, and no
runtime checks have passed. A multi-agent messaging bridge, unrelated MCP servers,
private memory services and public packaging are outside this slice. Distribution
and other-user installation remain M08. Planning does not authorize implementation.

## Handback

Report tested combinations, actual MCP/tool evidence, fallback behavior, the
controlled comparison and its limitations, generated-code checks and attribution.
Keep runtime delivery, simulated conduct, software correctness and human learning
as separate claims.
