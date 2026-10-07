# Optional Serena navigation

Mentor works with ordinary source reads, rg, diffs, edits and checks. Serena is
opt-in semantic navigation, independent of coaching profile and code ownership.
These helpers do not install packages, edit user configuration or create memories.

First inspect/reuse an existing registration:

```sh
python3 adapters/codex/serena/setup.py --workspace "/absolute/project"
```

If registered, verify its actual exposed tools/version in the host. Activate the
explicit project and inspect definitions/references/structure. Confirm memory,
onboarding and editing tools are unavailable for this integration. If the existing
connection cannot meet those constraints, use ordinary tools and document the
incompatibility; do not silently register a duplicate or overwrite configuration.

When absent, setup prints a snippet pointing to this checkout's launcher. Install
Serena separately using its [official setup](https://oraios.github.io/serena/02-usage/020_running.html)
and select a version. Review the printed host configuration before using it.
The default launcher requires an installed `serena` command:

```sh
python3 adapters/codex/serena/launch.py --workspace "/absolute/project" --check
```

`--executable` and repeated `--prefix-arg` support an explicitly chosen local
runner. Probing checks version/help only and never proves MCP delivery.
CLI probes use empty stdin so an interactive runner cannot consume the host's
initial MCP request before the server starts. Absent or incompatible servers
exit 2 with visible ordinary-tool fallback. Setup has no
implicit activation and writes no config. `navigation.yml` uses a fixed read-only
tool set; launch selects `no-memories`, `no-onboarding` and the tools interface.
Use `initial_instructions` to obtain the actual session token before project
activation when the exposed schema requires it. That read-only tool does not
authorize source edits, learner tracking or a change to Mentor's preferences.
See [configuration](https://oraios.github.io/serena/02-usage/050_configuration.html)
and [memory disabling](https://oraios.github.io/serena/02-usage/045_memories.html).

On 2026-10-07, Docker preflight was observed consuming the initial MCP request.
After isolating probe stdin, the real launcher initialized Serena
`2.0.0.dev0-3b99f8b0-dirty`. The corrected context exposes ten navigation tools,
including the read-only session instructions. Real calls returned structure,
definitions and references in a disposable Python project and activated a linked
worktree from another cwd. Editing, memory and onboarding tools were absent from
the exposed set. The stdin regression failed before the fix; all 26 Mentor tests
pass afterward. See [current evidence](../../../docs/evidence/M04-M07.md) for
native-host coverage and comparison limits. Direct MCP checks alone do not
establish native Codex delivery or efficiency.

Fresh native Codex turns subsequently verified actual model calls after the
connection/catalog was ready: ordinary paused source help and a matched build
comparison used the exposed read-only tools, including selected-project activation.
Both comparison candidates passed eight independent cases plus input preservation;
actual code/comments/docs were inspected. Readiness plus an exposed-tool discovery
request succeeded in these runs; this does not prove the cause of earlier model
routing failures. Recorded startup/time/token differences establish no efficiency
advantage. Preserve ordinary-tool fallback if a host/model cannot access the tools.

In the actual host, confirm `activate_project`, `find_symbol`,
`find_referencing_symbols` and `get_symbols_overview`, using its exposed schemas.
Activate another cwd/worktree explicitly. Language servers/backends may need
separate prerequisites; record the language, server and host versions and any
unsupported operation. Never invent navigation results. Project activation/indexing
may create Serena cache/config; use disposable project copies for Mentor trials.

For a bounded comparison, hold task, model, preferences and starter fixed. Record
actual startup overhead, calls, available time/tokens, resulting code/comments/docs
and behavioral checks with/without Serena. Missing metrics, unchanged/worse results
and unavailable runtime remain visible; no efficiency claim follows from setup.
