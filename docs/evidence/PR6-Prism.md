# PR #6 — optional Prism continuity and existing-server reuse

Follow-up requested on 2026-10-07 after the original M04–M07 delivery: use Prism
as Agentic Workflow does, preferring the existing native connection, and reuse
already available Serena/Prism rather than starting another instance/port.
The original [acceptance audit](M04-M07-acceptance.md) remains historical.

## Implemented behavior

- `adapters/codex/prism/context.py` inspects registrations read-only and prepares
  explicit load and requested project-summary/ledger/handoff tool arguments.
  It starts no service, selects no port, writes no local preference/binding, and
  reports prepared calls as `executed:false`. The primary agent uses exposed MCP
  tools; no duplicate transport client or server is created.
- The hook and four workflow context helpers supply optional command/guide paths.
  No startup Prism read/write is implicit. The guide retains dashboard context
  depth, project/conversation identity, supplied versions, explicit save/readback
  and partial-failure handling. Local Mentor reports/preferences remain authoritative.
- Prism inspection and Serena setup recognize launcher aliases and explicitly
  observed plugin/host connections. Existing/disabled registrations are preserved;
  incompatible/absent tools use local docs and ordinary navigation. No new port or
  duplicate registration is the fallback.

## Executable checks

`python3 -m unittest discover -s tests -v`: **29 tests passed in 13.593 s**.
New/expanded checks run the actual CLI process rather than asserting prose/source:

| Owner | Contract and credible regression | Why needed / seam |
| --- | --- | --- |
| Prism registration inspection | Aliased/disabled/configured and observed plugin connections reuse/fall back without configuration writes or fabricated live delivery; malformed config stays unchanged, secret env values stay out of output. | Existing tests covered no Prism entry point. A name-only detector could propose another server. No test-only production seam. |
| Prism load/requested-save boundary | Explicit project/conversation and observed version survive preparation; another workspace's binding is rejected, no local preference/file writes occur, calls remain unexecuted. | Wrong-project memory writes and implicit persistence are distinct from preference/report storage. Exercises the production CLI consumed by the primary agent. |
| Prism invalid records | Missing/invalid versions, malformed arrays, empty summaries and explicit learner/transcript fields yield nonzero with no tool request output. | Prevents bad requests and accepting reserved fields; free-form prose still needs agent inspection. No mock pretending to enforce server behavior. |
| Serena setup and relocated workflow context | Aliases/disabled/plugin connections preserve config and suppress another registration; relocated wrappers supply an executable optional command without disturbing saved preferences. | Extends the existing owners for new host-inventory and relocation risks; no duplicate helper-layer coverage. |

Raw current receipts are outside Git in `/private/tmp/mentor-pr6-prism-evidence/`
and `/private/tmp/mentor-pr6-prism-tests.txt`. No raw conversation is committed.

## Actual existing-host MCP checks

The current Codex connection is enabled stdio `npx -y
prism-mcp-server@20.21.17`. The adapter identifies it for inspection/reuse and
does not launch another server. Actual exposed tools, not config presence alone,
performed these checks under isolated project `mentor-pr6-prism-smoke-20261007`:

1. `session_load_context` returned fresh context with no version. The adapter
   prepared the same project/conversation binding with observed null version.
2. Requested fixture `session_save_ledger` saved the project-work summary;
   `session_save_handoff` created version 1. No learner data/grades/preferences
   were sent. This is an agent-authored software integration fixture.
3. Actual readback returned the exact summary, branch, context, TODO and recent
   session record. Optional semantic indexing was not queued; the morning-briefing
   LLM was not configured, neither of which prevented the primary memory result.
4. Another isolated project returned empty context, with no fixture summary.
5. A deliberately stale version-0 save with merging disabled returned `isError:true`.
   The server reported current version 2; subsequent readback preserved the original
   summary and TODO. No cause for the server's version advance is inferred.

These calls use the existing connection in this development host. This proves
the recorded load/save/readback subset, not all versions, providers, dashboard
features, semantic search or generic agent accuracy. The isolated fixture memory
is retained as a test record; pre-existing project handoffs were not replaced.

## Native hook coexistence and limits

The updated handler was reviewed/trusted through normal Codex 0.160.1 TUI in a
disposable workspace; no trust hash was manually supplied. Installed Workflow
hooks were retained. A fresh native gpt-6.1-sol/medium turn delivered the optional
Prism command/guide automatically and continued with local docs when Prism was
disabled and no opt-in supplied. No MCP or full Mentor skill was invoked in that
ordinary turn. Workflow's Stop hook blocked its first completion and a second
completion succeeded; no private hook was patched.

The separate native review turn verifies discovered explicit invocation and
missing-target clarification/wait without Prism writes: it executed the actual
skill context helper and asked for a target, then completed that clarification
turn without starting a review. Both native turns used zero MCP calls and created
no Mentor report/preference directory. Existing settings and
registrations remain unchanged apart from the disposable workspace's normal UI
trust records; user hook bytes and existing Prism Node processes match before/after.
The disposable hook/skill registrations were removed after the checks. Reusable
product files contain no personal toolkit dependency.
The MCP-disabled native probe does not prove automatic model use of Prism: actual
MCP evidence above comes from the primary agent's exposed connection. Human
learning, natural concurrent edits and broad transport/provider coverage remain
unobserved. M08 distribution remains separate.
