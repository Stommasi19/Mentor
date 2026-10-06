# Codex development adapter

`session_start.py` reads `core/policy.md` and `core/workflows/controls.md` relative
to its own location. It adds refreshed project defaults, warnings, and a pinned
control command. It accepts the native `SessionStart` JSON input on stdin and emits
`hookSpecificOutput.additionalContext` on stdout. It writes errors to stderr,
returns nonzero, and supplies no context if the event or core resource is invalid.
A preference failure preserves the valid policy and session controls with a
visible warning; a missing/invalid core resource fails the hook. A host can
continue after a hook error; do not interpret an open session as proof
that Mentor loaded.

It also validates `core/workflows/interview.md` and supplies its absolute trusted
path and a shell-quoted read command. The full interview instructions load when
needed rather than enlarging every session's context. A missing, empty, or
invalid-encoding interview resource fails visibly like the other core resources.

`development_config.py` prints a native hook definition with absolute, shell-quoted
interpreter and handler paths. It does not install anything or change trust.
The synchronous handler has a 5,000 approximate-token context limit, allowing
the policy, workflow and settings to arrive together. Codex's
[hook output limits](https://learn.chatgpt.com/docs/hooks#large-hook-output)
can spill larger context to a file. This prototype uses Python's standard library
and POSIX shell quoting. Windows
and other hosts remain unverified. Moving the checkout or interpreter requires
regenerating the configuration and reviewing the changed hook.

For a disposable external workspace, from the Mentor checkout:

```sh
mentor_workspace=$(mktemp -d)
cp fixtures/expense-summary/starter/*.cs fixtures/expense-summary/starter/*.csproj "$mentor_workspace/"
cp fixtures/expense-summary/scenarios/S01/task.md "$mentor_workspace/TASK.md"
mkdir -p "$mentor_workspace/.codex"
python3 adapters/codex/development_config.py > "$mentor_workspace/.codex/hooks.json"
codex -C "$mentor_workspace"
```

Use the host's normal project trust flow, then `/hooks` to inspect and trust the
generated command. Start a fresh session after trusting it and request the task
in `TASK.md`. Do not paste the
policy or invoke a skill to claim automatic delivery. Inspect the host's actual
execution and delivered developer context, and exercise S01. Disable the hook
through `/hooks` and repeat in a fresh session as a negative control. No global
hook, plugin manifest, marketplace entry, or trust-store edit is needed.

## Interview coaching

Ask naturally: “Use Mentor's interview workflow to clarify this task.” The agent
reads the canonical resource using the hook-provided location and applies the
current task, effective level/coaching state, project agreements, and previous
reasoning. It can also use the workflow when requirements uncertainty warrants
deeper clarification. No private skill installation or custom slash command is
required. Explicit invocation on a fully specified task proceeds proportionately.

For example, “Make Mentor ask fewer questions” needs a decision about when a
question changes the next step; Mentor can help clarify that rule and a check.
Paused coaching retains necessary clarification without forcing an exercise.
“Please implement directly” keeps implementation with the agent at any level.
An interview request alone does not authorize code changes. Decisions, remaining
assumptions, and verification stay in the conversation or normal task document;
the workflow does not write preferences or a learning ledger.

See [M03 evidence](../../docs/evidence/M03.md) for tested invocation, conduct, and
limitations. Spending in the external fixture is a sample coding task, not a
Mentor product feature. Public packaging/discovery remains M08.

## Local controls and storage

Before launching the host, optionally set `MENTOR_DATA_DIR` to an absolute path;
the default is `<user-home>/.mentor`. The hook canonicalizes that root and the
workspace identity using the [shared helper](../../runtime/README.md), then
supplies the interpreter, control path, project ID and data root explicitly.
Relative/invalid configuration or unavailable identity warns and disables saving
without choosing another location. Settings live outside the repository; no
storage is created by startup, status, or session-only controls.

Ask naturally: “use supported”, “pause coaching”, “resume coaching”, “show Mentor
status”, or “use project preferences again”. These affect only this conversation.
“Use independent for this project”, “save coaching off as this project's default”,
and “reset this project's preferences” explicitly request writes. Demonstration,
takeover and task-specific help do not change preferences. No custom slash command
is required.

The agent runs the delivered base shell command with the current session object:

```sh
# Replace these example locations with the exact hook-provided values.
/absolute/python3 /absolute/Mentor/adapters/codex/control.py \
  --project-id PROJECT_ID_FROM_HOOK --data-root /absolute/local-data \
  --session '{"overrides":{},"unsaved":[]}' set-level independent
```

Other action forms: `pause`, `resume`, `status`, `use-project`,
`--field level use-project`, `--field coaching_enabled use-project`,
`--scope project set-level supported`, `--scope project pause`, and
`--scope project reset`. Options may precede the action. Quote session JSON for
the shell. Use the returned `session` object on the next call; the helper cannot
discover another conversation's context. Apply `effective` immediately and report
scope, effective/saved differences and warnings. Exit zero with `persisted:false`
means a valid request applied locally but was not saved; rejected actions exit
nonzero and emit no result. Shell/tool environments need no `MENTOR_DATA_DIR`
because the command already contains the resolved location.

Resume/manual compaction retain the conversation's session object while reloading
project defaults. Clear starts without overrides. Status refreshes saved settings
without removing overrides. Another open conversation adopts changed project
defaults on status/control or lifecycle delivery, retaining its own choices.
There is no live broadcast. Invalid records require explicit project reset;
failed saves/resets apply locally as unsaved overrides and preserve the prior
record. Atomic writes use last-completed-write semantics, without concurrent
field merging. See [state contracts and limitations](../../runtime/README.md).

The [M02 evidence report](../../docs/evidence/M02.md) distinguishes process checks
from native startup/resume/manual-compaction/clear, actual control invocation,
and two-session refresh. Automatic mid-turn compaction remains separately pending.

See the [official hook reference](https://learn.chatgpt.com/docs/hooks) for hook
discovery, review/trust, event schemas, developer-context delivery, and output
limits. This adapter uses synchronous delivery and the configured 5,000
approximate-token limit; keep the core concise. See [M02 verification](../../docs/evidence/M02.md)
for current tested versions/events and [M01 verification](../../docs/evidence/M01.md)
for historical results.

Run the adapter contract checks from Mentor:

```sh
python3 -m unittest discover -s tests -v
```

The checks run the generated command from another directory, including checkout
paths with spaces, an apostrophe, and a dollar sign. They also exercise missing,
empty, invalid-encoding resources, invalid events/controls, real project identity,
field precedence and storage failures. They do not simulate a host trace or
certify generated code quality.
