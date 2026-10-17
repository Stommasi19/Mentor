# PR #6 — missing-tool setup and separate Mentor memory

Follow-up requested on 2026-10-07: provision requested missing Prism/Serena,
then keep Mentor's Prism separate from Agentic Workflow. This supersedes the
shared-backend default in the [earlier reuse receipts](PR6-Prism.md). The original
M04–M07 acceptance audit remains historical. No DoughTracker source is changed.

## Implemented behavior

`adapters/codex/setup_mcp.py` previews without writes and, on requested `--apply`,
provisions missing compatible connections through the actual `codex mcp add`
writer. Existing settings, disabled registrations, aliases and observed plugin
connections are preserved. Repeated apply reuses registrations; partial success
is reported rather than undone or fabricated. Registration remains explicitly
`live_connection_verified:false`, and setup starts no MCP session. The host must
reload and expose actual tools. Hooks advertise the pinned command, not an
automatic installer. Core/manual preferences/report ownership are unchanged.

Default Prism storage is a dedicated Docker volume at `/root/.prism-mcp`, where
the installed upstream local backend actually stores its memory database. The
stdio launcher publishes no host port, mounts no host memory directory, inherits
no cloud credentials and uses `--network none`. Shared Workflow Prism remains
intact. A verified dedicated connection is reused; a shared `mentor_prism` is
preserved while a missing dedicated connection is named `mentor_prism_isolated`.
Docker unavailability does not fall back to shared memory. Explicit shared mode
is available for users who choose it, with the shared-storage limitations stated.
Prepared loads/saves retain the actual server namespace, workspace, selected
project/conversation and supplied version; old bindings without a namespace fail.

Missing Serena uses an installed runner or local pinned uv/Serena provisioning.
Its launcher makes locally installed uvx discoverable to language-server child
processes without changing shell/global PATH. Navigation excludes editing,
memories and onboarding. Readable names, intent comments, failure messages and
the [setup guide](../../adapters/codex/MCP-SETUP.md) describe the actual lifecycle.

## Actual fresh provisioning and MCP observations

Commands ran against a disposable workspace and Codex home under
`/private/tmp/mentor-pr6-mcp-setup`, using this PR worktree's actual launchers.
No fake tool outputs or model-written pass receipts were supplied.

1. Fresh Serena provisioning installed `uv==0.12.23` into the disposable home's
   local tools environment and cached 78 dependencies from pinned Serena commit
   `3b99f8b024dafd58c962ea6e74f37c8a730ef532`. Its actual CLI/server reports
   `2.0.0.dev0`. Codex's native writer created the registration and readback
   matched. A first-run missing-home failure was reproduced and fixed by creating
   the selected home only on the requested write path.
2. Requested separate Prism setup built the repository image with actual
   `prism-mcp-server@20.21.17` on Node `22.23.3`, then registered
   `mentor_prism_isolated`, preserving an existing shared fixture registration.
   Native readback reported `registered`, `server_started_by_setup:false` and
   `live_connection_verified:false`. An earlier temporary shared registration
   used an invalid `PRISM_STORAGE=sqlite`; installed-source inspection corrected
   product setup to the supported value `local`. That old fixture was preserved
   for nonmutation proof and never used as a runtime connection.
3. A disposable JSON-RPC MCP observer launched that actual registered dedicated
   Docker command, initialized it and inspected real tools. Under project key
   `mentor-pr6-database-isolation-proof-20261007`, actual ledger/handoff saves
   succeeded, then actual load returned:

   ```text
   Last Summary: Dedicated Mentor database fixture: calculate_total returns the sum of supplied amounts.
   Open TODOs:
     - Fixture only; no learner participation observed.
   ```

4. The already exposed Workflow/shared Prism connection loaded the **same key**
   before and after the dedicated save. Both actual results were:

   ```text
   No session context found for project "mentor-pr6-database-isolation-proof-20261007" at level standard.
   This project has no previous session history. Starting fresh.
   ```

   This proves tested database separation beyond using two different project
   keys in one database. Shared connection tests were reads; no shared fixture
   write was made for this isolation check.
5. Actual Docker inspection of the running dedicated process reported network
   mode `none`, empty port bindings, one volume mount named
   `mentor-prism-smoke-20261007` at `/root/.prism-mcp`, and only local storage plus
   base image environment variables. No host bind mounts or cloud credentials
   were present. The observer closed its stdio clients; the test container exited
   and its owned test volume was removed. The built dependency image is retained.
6. The fresh registered Serena command initialized and exposed the expected
   navigation tools. Its first actual symbol call failed because child language
   servers could not find locally installed uvx in PATH. After the launcher fix,
   the same real connection reported `Language server status: ready`, read the
   disposable `example.py` and returned `{"Function": ["calculate_total"]}`
   from `get_symbols_overview`. The observer ended with:

   ```text
   PASS: dedicated Prism roundtrip/container isolation and fresh native Serena file/symbol reads
   ```

7. Repeated actual `setup_mcp.py --server both --apply` returned only
   `inspect-and-reuse` for the dedicated Prism and Serena registrations. The old
   shared fixture was not selected as compatible dedicated storage.

Receipts, initial failures, JSON-RPC traffic, observed container config and
shared negative controls are retained outside Git in
`/private/tmp/mentor-pr6-mcp-setup/`. The observer is an integration fixture, not
a Mentor user workflow or a claimed learner contribution. Ordinary user Codex
registrations were not modified by these provisioning checks; native Serena may
write its normal runtime/project metadata while navigating the disposable project.

## Boundary checks and test authoring gate

```text
python3 -m unittest discover -s tests -v
Ran 33 tests in 15.129s
OK
```

Python compilation and `git diff --check` passed. All 263 relative Markdown
file links resolved. Actual Codex CLI version: `0.160.1`. These checks ran on
the final product/test source in the PR worktree; documentation receipts were
then added without changing implementation.

The current suite runs the real entry points and actual Codex configuration writer.
Serena's installed-CLI fixture in unit tests probes CLI/config handling only and
explicitly never supplies MCP responses; real semantic proof is the runtime
observation above. No production test-only injection seams were added.

| Test owner / gate result | Protected contract and regression | Existing coverage gap / boundary |
| --- | --- | --- |
| Missing registration, pass | Preview is read-only; requested apply preserves unrelated settings and native readback; repeated apply neither rewrites nor installs. Wrong scope/duplicate provisioning would fail. | Existing setup covered preview only; runs the actual native writer in a disposable home. |
| Alias/plugin/disabled/malformed config, pass | Known connections suppress provisioning and malformed settings remain intact. Name-only detection/overwriting would fail. | Extends setup owner for provisioning decisions; no simulated live server. |
| Separate storage and unavailable Docker, pass | Shared Workflow connection is not reused as dedicated; dedicated alias is reused; no shared fallback/write when Docker is absent. | New dedicated-memory contract; CLI process boundary and real environment, not a mocked guard. |
| Partial failure, pass | Completed Prism registration remains visible when Serena fails; retry reuses it. Missing Codex home is created on the actual write path. | Distinct failure path, reproduced failure before fix; actual native writer. |
| Prism namespace/alias requests, pass | Actual server namespace survives load/save; missing namespace rejects saves; dedicated launcher alias is discoverable without starting it. | Extends existing request/inspection tests, avoiding duplicate helper-layer tests. Alias regression failed before its detector fix. |

Fresh Serena's runner regression failed on the pre-fix actual MCP symbol call
and passed on the same real boundary after repair. CLI registration/unit tests
alone could not reach this child-process dependency failure.

## Limits

The new provisioning/runtime checks use direct JSON-RPC observers of actual
registered commands, not a model automatically selecting newly reloaded MCP tools.
Earlier [native host coexistence receipts](PR6-Prism.md) remain valid for the
previous hook revision; the new setup/isolation guidance is checked at the
process boundary, with its fresh native model-delivery observation pending.
Codex registration is not itself host runtime delivery. This is the recorded
macOS/Python/Codex/Node/Docker and pinned Serena/Prism combination, not universal
compatibility. Network-disabled Prism proves local history, not cloud/embedding
features or model behavior. Database separation protects ordinary connection
access, not a host administrator. Human participation/understanding is unobserved.
M08 public installation/distribution remains future work.
