# Private plugin closeout — 2026-10-17

Publication attempt: the completed follow-up could not create its new remote
branch. GitHub returned “MCP tool call requires approval, but approval policy is
never”. No new branch or PR was created. A local commit, bundle, two-commit patch
and PR description are prepared for publication through an approved connection.

After PR #6 merged, the user requested a new PR for any missing work, keeping
public release deferred. The remaining implementation is saved manual coding
mode (not included in PR #6) and a native private Codex package. Work is isolated
on `feat/private-plugin-closeout`, based on merged main
`783dede2f4a477ecbffd92eb63636c76cf55ce35`. The original dirty checkout and external
projects are preserved. No public directory submission or release was performed.

## Package and checks

The Codex compatibility manifest points to the existing adapter skills and hook
file. The local `mentor-private` catalog exposes that root package. Core/runtime
and workflow source remain canonical; no personal checkout path or copied policy
is embedded. Optional MCP setup is retained without installing/starting services
when the plugin is installed. See [private usage](../PRIVATE-INSTALL.md).

Executed on macOS arm64 with Python 3.14 and Codex CLI/app-server 0.160.1:

```text
python3 -m unittest discover -s tests -v
Ran 36 tests in 19.420s
OK
```

No tests skipped. Python syntax parsing, `git diff --check` and all 284 relative
Markdown file links passed. The suite
includes the prior 35 manual-mode/MCP/report/target/workflow checks and one new
native private-package lifecycle test.

The actual installer failed before packaging with “marketplace root does not
contain a supported manifest”. After adding the package and local catalog:

- `codex plugin marketplace add <source> --json` registered `mentor-private` in a
  disposable `CODEX_HOME`; `plugin add mentor@mentor-private --json` installed
  version 0.1.0 into that home's cache; native list reported installed/enabled.
- The configured cached hook supplied a working control command. An explicit
  manual-mode fixture save reported verified persistence. With the authoring
  source renamed out of the way, all four cached context entry points executed,
  resolved workflows inside the installed cache and retained manual preferences.
- A disposable source update to 0.1.1 and changed policy was installed by the
  native installer. Cached hook output contained the changed policy and saved
  manual mode. No editing of cache files was used to manufacture an update.
- Changing the actual host config to disabled was reflected in native inventory;
  restoring it re-enabled the package. A transient CLI `-c` override did not
  affect this CLI listing, so saved configuration is used in the documented check.
- Native uninstall left no installed entry or current package cache, while the
  external manual preference record stayed byte-identical. Unrelated model/MCP
  configuration was preserved. All mutations were inside disposable fixtures.

These configured-hook/context executions are real process checks, not proof that
Codex automatically delivered a trusted hook to a model.

## Native host discovery and the corrected naming mismatch

A real app-server initialized with the privately installed package, then performed
`plugin/list`, `skills/list`, `hooks/list` and `thread/start`. No model turn or
manually supplied policy was used. Actual results included:

- `mentor@mentor-private`: installed and enabled, with no marketplace load errors.
- Four cached skills named `mentor:mentor-interview`, `mentor:mentor-review`,
  `mentor:mentor-feedback` and `mentor:mentor-pr-check`.
- The plugin's SessionStart hook, its expanded cached path, four-source matcher,
  timeout and context limit. Its trust status was **untrusted**, as expected for
  a new installation.

This exposed a real adapter mismatch: development guidance advertised bare skill
names while native installed skills had a `mentor:` namespace. The hook now
advertises namespaced names when `PLUGIN_ROOT` identifies plugin execution and
keeps bare names for development registration. The final lifecycle check executes
the cached hook and verifies those public invocation identifiers.

A normal TUI `/hooks` attempt could not reach trust review: bootstrap failed with
`account/read failed: workspace routing discovery failed (code -32603)`. No trust
hash was written manually and no bypass flag was used. The temporary host was
isolated; any temporary authentication copy used for this attempt was removed.
The host's real startup result was not counted as trusted hook delivery.

## Authoring gate and scope

The new lifecycle test passes the testAudit authoring gate: it protects the actual
native installation/cache/update/removal boundary against missing manifests,
checkout coupling, stale policy and preference/config loss. Existing direct
adapter tests cannot reach that native cache lifecycle. The test uses actual
Codex and filesystem operations, no simulated success responses or production
test-only seams. Namespace assertions protect the public identifiers observed
in actual host discovery. The pre-package rejection and corrected path are both
retained.

Raw fixture receipts are under `/private/tmp/mentor-private-package-check/`,
including `before-package.txt`, `lifecycle-test.txt`, `full-suite.txt`, native
app-server responses and protocol observations. Raw credentials and conversations
are not committed. The package format follows
[official OpenAI documentation](https://developers.openai.com/plugins/build/plugins)
and the installed host's CLI/schema; support is limited to the tested combination.
The disposable plugin/catalog registrations were removed after observation;
temporary authentication was absent at cleanup. Learner preference fixtures and
receipts remain available without an active test installation.

## Remaining observations

Trusted automatic hook delivery and a live manual-mode guidance/review session,
including a requested demonstration and return to manual ownership, remain pending
for this revision because TUI startup could not complete. New MCP setup has its
[recorded direct runtime evidence](PR6-MCP-setup.md), not a new automatic model-use
claim. Other platforms/providers and human-learning outcomes are unobserved.
Public installation, catalog submission, release assets and publication remain
deferred. The private package's successful native lifecycle/discovery does not
mark every M08 distribution acceptance criterion complete.
