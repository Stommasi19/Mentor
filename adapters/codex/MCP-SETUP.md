# Optional development MCP setup

Prism and Serena remain optional. Inspect actual host tools and registrations
before setup. Reuse existing Serena and verified dedicated Mentor Prism connections,
including aliases and plugin connections. Workflow's shared Prism is preserved
but is not compatible with Mentor's default separate memory requirement.

Run from this development checkout, supplying the project to navigate:

```sh
python3 adapters/codex/setup_mcp.py --workspace /absolute/project
python3 adapters/codex/setup_mcp.py --workspace /absolute/project --apply
```

Without `--apply`, preview reads configuration and reports missing connections;
it writes no config or dependencies. `--server prism|serena|both` limits scope.
`--codex-home /absolute/codex-home` selects the host config/tools directory; the
default respects `CODEX_HOME`. The hook supplies a command pinned to its actual
workspace and home because tool environments can differ from the hook environment.

For a compatible connection already exposed by a plugin but missing from config,
pass `--connected-prism NAME` or `--connected-serena NAME`. These are statements
from observed host inventory, not probes. For Prism, verify the connection uses
dedicated Mentor storage before passing it. Existing disabled registrations are
reported for inspection without overwriting or launching a replacement.

On requested apply, the helper provisions only missing connections:

- Prism requires installed, running Docker. It builds `mentor-prism:20.21.17`
  from the repository Dockerfile if absent. Codex launches the stdio container
  on demand with `mentor-prism-data`, no host ports, no host bind mounts, no
  inherited cloud credentials and no network. `--prism-volume NAME` chooses
  another dedicated Docker volume, not a host filesystem path. Repeated setup
  reuses a registered dedicated connection; changing volume requires reviewing
  that existing registration, not silently creating another one.
- Serena prefers an installed `serena`, then installed `uvx`. If both are absent,
  it creates a local Python environment under the selected Codex home's
  `mentor-tools/uv`, installs pinned `uv==0.12.23`, and caches Serena from commit
  `3b99f8b024dafd58c962ea6e74f37c8a730ef532`. The launcher exposes navigation tools
  with memories, onboarding and editing excluded. Its child processes can find
  the local runner without editing the user's shell PATH. Language servers may
  download their own dependencies; unsupported languages retain ordinary tools.

The helper uses `codex mcp add` and reads its registration back, preserving other
servers/settings. An occupied shared `mentor_prism` remains intact; the dedicated
registration becomes `mentor_prism_isolated`. An incompatible collision there
requires inspection. Partial setup reports each outcome and retains the successful
registration so retries reuse it. A malformed config is never replaced.

Dependencies can require network access during installation. The helper does not
install Docker, Node/npm or Codex globally. `--prism-memory shared` explicitly
chooses shared storage and allows native pinned Node/npx provisioning when absent;
it must not be used as an automatic fallback from dedicated memory.

Restart/reload Codex after registration. Inspect actual exposed tools, initialize
the selected connection, verify the workspace/backend and perform a real read.
Registration and CLI version probes are not proof of live MCP delivery. Setup
itself starts no MCP session. Keep requested Prism saves bound to the actual
dedicated connection in [the Prism guide](prism/README.md). When unavailable,
continue Mentor using local docs and ordinary checks.

This is development integration. Public installation/distribution remains M08.
