# Optional Prism project continuity

Mentor uses a dedicated Prism database by default, separate from Agentic Workflow.
Load project context, then save a project-work summary and handoff when requested.
The host launches the repository's stdio Docker adapter with a named volume,
`mentor-prism-data`, mounted at Prism's actual memory directory. It publishes no
host port, mounts no host memory directory and inherits no cloud credentials.
The container has no network access. Workflow's Prism connection and data remain
unchanged. This separates storage accessible through the ordinary connections;
it is not protection against someone who controls Docker or the host machine.

Prism is opt-in for the current conversation. “Use Prism project PROJECT for this
workspace” authorizes context loading; “save this project handoff to Prism”
authorizes a summary and handoff write. Reuse that project selection on subsequent
loads in this conversation. Clear requires a new opt-in; never change Mentor's
level/preferences or create a learner ledger. Ordinary help and explicit Mentor
skills work with Prism disabled, absent, incompatible or unavailable.

## Inspect and reuse

First inspect the host's available MCP connections and tools. A registration is
not proof of a connected server. The helper reads host config without writing it:

```sh
python3 adapters/codex/prism/context.py --workspace /absolute/project inspect
```

It uses `CODEX_HOME/config.toml`, or the ordinary user Codex home when unset.
Use `--config /absolute/config.toml` for another reviewed config. For a host/plugin
connection missing from that file, pass `--connected-server NAME` after observing
it in the actual host inventory. Aliased native Prism launchers are recognized.
Inspect identifies candidates, including shared servers; it does not prove storage
isolation. Reuse a verified dedicated Mentor connection. Pass a plugin connection
to setup only after verifying its storage is separate from Workflow. A disabled
dedicated registration requires inspection or fallback, rather than a duplicate.

If no compatible dedicated connection exists, use the [MCP setup guide](../MCP-SETUP.md):

```sh
python3 adapters/codex/setup_mcp.py --workspace /absolute/project --server prism --apply
```

This builds the pinned Prism image if absent and registers a missing connection
through Codex's native writer. It preserves shared registrations, using
`mentor_prism_isolated` if `mentor_prism` is already occupied. Docker must be
installed and running; failure retains local docs, never silently shared memory.
The setup command does not start an MCP session. Restart/reload the host, then
verify tools and the selected backend. Hooks themselves install/start nothing.

`--prism-memory shared` is an explicit alternative for users who choose Workflow's
storage; it reuses existing connections or registers pinned native Node/npx Prism
when missing. Different project keys in a shared database are logical organization,
not access control. Do not choose this option for the requested separation.

## Load actual project context

Choose the exact existing Prism project key with the user; repository names alone
can collide. Agentic Workflow uses a remote owner/repository slug when available.
Do not silently change that key to Mentor's neutral workspace ID. Use a unique
conversation ID consistently for the load and saves (reuse the host's Prism ID if
available). Prepare a request from any cwd using the hook-pinned helper:

```sh
python3 adapters/codex/prism/context.py --workspace /absolute/project load \
  --project OWNER-REPOSITORY --conversation-id CURRENT_CONVERSATION \
  --server-name ACTUAL_DEDICATED_CONNECTION
```

The JSON describes an unexecuted `session_load_context` request and a workspace
binding, including the actual server namespace. The primary agent executes it
through that connection's **already exposed host tool**, using its actual schema.
Never substitute Workflow's connection when Mentor's is unavailable. Keep the
configured context depth by omitting `level`;
limit returned context to 2,000 approximate tokens. Do not send a prompt that
implicitly routes new skills. Retrieve additional specific context only as needed.
Label retrieved notes as Prism project context, verify the project, and keep them
subordinate to current instructions, code and check evidence. Returned skill text
does not explicitly invoke a full Mentor interview, review or feedback workflow.

After a successful load, retain the returned session binding in conversation
context and add `expected_version` from the actual response. Use null only when
that response supplies no version (for example, a fresh project). Do not fabricate
zero or mark an unsuccessful load as loaded. No local binding/preferences are saved.

## Requested project save and readback

Provide a JSON record on stdin to `save --session '<binding JSON>'`: required
`summary`, optional string arrays `todos`, `decisions`, `files_changed`, and optional
`active_branch`/`key_context` strings. Include project facts and local report paths
when useful. Exclude transcripts, learner answers, grades, inferred ability,
coaching levels and preference records; field validation cannot inspect prose for
all such content, so the primary agent reviews the summary before sending it.

The helper rejects another workspace's binding, a missing server namespace and
unknown fields, and prepares
`session_save_ledger` and `session_save_handoff` calls; `executed:false` is not save
success. Execute through the existing host connection only after the user's save
request. Preserve the observed version and disable automatic merge so a concurrent
handoff cannot silently replace agreed context. On a conflict, reload, inspect
the current handoff and reconcile the requested project facts before retrying.
Run the calls sequentially and inspect each result, stopping on an error. A fresh
load with no supplied version has no version-based concurrency protection; keep
that limitation visible rather than inventing a version or claiming a locked save.
If context expires, reload the same project/conversation before retrying once.
The two calls are not atomic: report partial success honestly; do not blindly
repeat an already saved ledger entry. Reload to verify the actual summary, TODOs
and history before claiming success. Leave an unperformed/failed save visible and
continue ordinary Mentor work with local documents. Local Markdown reports and
manual preferences remain authoritative.

## Source and verification

This adapts Agentic Workflow's [session context/close pattern](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/skills/_preamble.md)
without importing its private paths or making its fail-on-unavailable behavior a
Mentor dependency. Actual host schemas and versions determine compatibility.
See the [original reuse evidence](../../../docs/evidence/PR6-Prism.md) and
[dedicated setup evidence](../../../docs/evidence/PR6-MCP-setup.md) for performed
calls, nonmutation checks, failure controls and remaining limits.
