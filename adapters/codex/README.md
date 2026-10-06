# Codex development adapter

`session_start.py` reads the single shared `core/policy.md` relative to its own
location. It accepts the native `SessionStart` JSON input on stdin and emits
`hookSpecificOutput.additionalContext` on stdout. It writes errors to stderr,
returns nonzero, and supplies no context if the event or core resource is invalid.
A host can continue after a hook error; do not interpret an open session as proof
that Mentor loaded.

`development_config.py` prints a native hook definition with absolute, shell-quoted
interpreter and handler paths. It does not install anything or change trust.
This prototype uses Python's standard library and POSIX shell quoting. Windows
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

The configured matcher covers startup, resume, clear, and compact. Handler tests
for those values establish the output contract; each native lifecycle still
needs its own observed trace. Explicit conversation choices must survive reloads;
persistent preferences and controls are M02.

See the [official hook reference](https://learn.chatgpt.com/docs/hooks) for hook
discovery, review/trust, event schemas, developer-context delivery, and output
limits. This adapter uses synchronous delivery and the host's default context
limit; keep the core concise. See [verification results](../../docs/evidence/M01.md)
for the exact version and events actually tested.

Run the adapter contract checks from Mentor:

```sh
python3 -m unittest discover -s tests -v
```

The checks run the generated command from another directory, including checkout
paths with spaces, an apostrophe, and a dollar sign. They also exercise missing,
empty, invalid-encoding resources and invalid event input. They do not simulate a
host trace or certify generated code quality.
