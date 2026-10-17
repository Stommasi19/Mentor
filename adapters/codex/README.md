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

It also validates the interview, review, feedback and PR-understanding workflows
and supplies concise explicit-only native skill guidance. Full instructions load through skill invocation
rather than enlarging every session's context. A missing, empty, or
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

The revised `$mentor-interview` is a native, explicit-only skill. Register its
thin wrapper in a disposable development workspace, keeping the canonical core
in this checkout. Codex supports repository `.agents/skills` discovery and
symlinked folders; `agents/openai.yaml` disables implicit invocation. See the
[official skill guide](https://learn.chatgpt.com/docs/build-skills).

From the Mentor checkout, after choosing the absolute `mentor_workspace`:

```sh
mkdir -p "$mentor_workspace/.agents/skills"
ln -s "$PWD/adapters/codex/skills/mentor-interview" \
  "$mentor_workspace/.agents/skills/mentor-interview"
```

This is local development registration, not a public installer or plugin manifest.
Keep an existing link unless you intend to replace it. Moving the checkout requires
updating this link as well as regenerating the hook configuration. Start Codex in
that workspace, use `/skills` or the `$` selector, and explicitly select
`$mentor-interview`. The hook delivers concise discovery guidance but does not
register the skill. Ordinary tasks retain necessary clarification without running
the full interview or writing interview artifacts.

Example: “$mentor-interview Help define the monthly/category calculation;
requirements-only, 30 min, no UI. Explain consequential choices with examples.”
For implementation, explicitly specify direct execution or an available target
skill. Known requirements and participation agreements are reused. The primary
agent handles staged questions, teaching preferences, drill-down, and a concrete
summary. Settled tasks and skip requests avoid invented rounds. Paused coaching
retains requirements, confirmation, and artifacts with direct clarification.

The wrapper's `scripts/context.py` resolves the real checkout through the symlink,
validates the canonical policy/workflow, and refreshes M02 status without writing
preferences. It receives the current conversation session JSON and the hook's
pinned data root when available. Without hook context, it uses the explicit
`--data-root`, otherwise `MENTOR_DATA_DIR`, otherwise `<user-home>/.mentor`.
It supplies shell-quoted commands and resource paths; tools may run from another
cwd. Invalid locations fail visibly without silently selecting another root.

Each invocation reserves a task directory under
`<data-root>/projects/<project-id>/plans/<date>-<task-slug>/`, with numeric suffixes
on collisions. `interview.md` records the original request, target, verbatim time
box/scope, questions and actual answers throughout. The confirmed `plan.md` records
understanding, approach, teaching plan, scope, assumptions, and acceptance checks,
with a pointer to the interview. Full transcripts stay outside public Git.

Execution waits for confirmation of the concrete plan; prior explicit approval
of that same plan satisfies the gate. After both files are saved and read back,
already-authorized work proceeds without another blanket gate. Requirements-only
ends with artifacts and leaves code untouched. A selected skill receives the
original request, constraints, and both artifact references, and runs through
the primary agent. Missing/incompatible targets require a resolved replacement.

`artifacts.py` supports `create --task LABEL`, `append --directory PATH` with
Markdown on stdin, and `finalize --directory PATH --confirmation TEXT` with plan
Markdown on stdin. Use the exact returned command and directory. Failed saves
exit nonzero and emit no success JSON; partial files can remain, so inspect and
repair them before retrying or continuing. A successful write does not itself
certify plan accuracy or user authorization; the agent verifies those separately.

See [revised M03 evidence](../../docs/evidence/M03-revised.md) for native invocation,
conduct and limitations; [original M03 evidence](../../docs/evidence/M03.md) remains
historical. Public packaging/discovery remains M08.

## Local controls and storage

Before launching the host, optionally set `MENTOR_DATA_DIR` to an absolute path;
the default is `<user-home>/.mentor`. The hook canonicalizes that root and the
workspace identity using the [shared helper](../../runtime/README.md), then
supplies the interpreter, control path, project ID and data root explicitly.
Relative/invalid configuration or unavailable identity warns and disables saving
without choosing another location. Settings live outside the repository; no
storage is created by startup, status, or session-only controls.

Ask naturally: “use Mid-level”, “pause coaching”, “resume coaching”, “show Mentor
status”, “use manual coding”, “use assisted coding”, or “use project preferences
again”. These affect only this conversation.
“Use Senior for this project”, “save coaching off as this project's default”,
“save manual coding for this project”, and “reset this project's preferences”
explicitly request writes. Manual mode gives guidance/hints/reviews without
project implementation edits or complete solutions unless explicitly requested;
it applies at every level and while coaching is paused. Demonstration,
takeover and task-specific help do not change preferences. No custom slash command
is required.

The agent runs the delivered base shell command with the current session object:

```sh
# Replace these example locations with the exact hook-provided values.
/absolute/python3 /absolute/Mentor/adapters/codex/control.py \
  --project-id PROJECT_ID_FROM_HOOK --data-root /absolute/local-data \
  --session '{"overrides":{},"unsaved":[]}' set-level senior
```

Other action forms: `pause`, `resume`, `status`, `set-coding-mode manual`,
`set-coding-mode assisted`, `--scope project set-coding-mode manual`, `use-project`,
`--field level use-project`, `--field coaching_enabled use-project`,
`--field coding_mode use-project`,
`--scope project set-level mid-level`, `--scope project pause`, and
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

## Review, feedback and PR understanding

The three new native skills use the same development registration as interview.
After choosing a disposable or authorized target workspace, register their folders
without replacing existing links:

```sh
for mentor_skill in mentor-review mentor-feedback mentor-pr-check; do
  ln -s "$PWD/adapters/codex/skills/$mentor_skill" \
    "$mentor_workspace/.agents/skills/$mentor_skill"
done
```

The target's `.agents/skills` directory must already exist. Review any existing
registration instead of overwriting it. This is development setup, not M08 public
installation. Invoke through the host's `$` selector:

- `$mentor-review Review staged changes; run relevant checks.` With no target,
  Mentor asks what to review. Coaching-on primes and waits; “show findings” skips.
  The workflow reports findings and saves Markdown without fixing/posting.
- `$mentor-feedback Give feedback on this task.` Feedback is immediate;
  reflection is optional, with a separate local report and no automatic review.
- `$mentor-pr-check https://github.com/OWNER/REPO/pull/NUMBER` reads actual PR
  source, asks focused questions and supports hint, explanation, skip and stop.
  Unattempted and assisted answers remain visible. It does not approve or edit.

Each wrapper resolves canonical resources through its real folder, refreshes
preferences read-only with the current `--session`, and returns quoted control,
report and target commands. Pass the hook-pinned data root; invocation never loses
session overrides. Reports live under the configured project data root:
`reviews/<date-task>/review.md`, `feedback/<date-task>/feedback.md`, or
`pr-checks/<date-task>/pr-check.md`. Reserve with `create --task LABEL`; save with
`save --directory RETURNED_PATH` and Markdown on stdin. Successful saves are
read back and never replace an existing report. Failures remain visible.

`review_target.py local --workspace /absolute/repo --scope staged` captures actual
index content. Other explicit scopes: `unstaged`, `uncommitted` (including untracked),
`range --base REF [--head REF]` using the merge base. Repeated `--path` filters
literal repository-relative paths. Output includes before/after contents, modes,
renames/deletions, per-layer diff and a content snapshot ID. Re-run after a pause;
changed IDs invalidate affected evidence. Run checks in disposable copies at the
captured content; a worktree check cannot certify different staged code.
Submodule commit changes can be captured. Dirty submodule contents require a
separate local target; the helper fails rather than treating status filenames as
an identity for the changed code.

`review_target.py pr --url https://github.com/OWNER/REPO/pull/NUMBER` uses read-only
GitHub CLI API calls, complete paginated filenames, merge-base/head file context,
fork identity and revision refresh. Missing CLI/auth/network, incomplete context
or changed PRs fail visibly. The primary agent may use an available read-only GitHub
connector instead, recording actual transport and pinned evidence separately.
Neither transport is required for ordinary source explanations.

Profiles use `junior`, `mid-level`, `senior`. Legacy `guided`, `supported`,
`independent` remain control aliases. Valid version-1 preferences and retained
legacy sessions translate read-only; status identifies their legacy values.
Only explicit project changes/reset write canonical version-2 preferences. The
profiles change task focus while readable code, useful comments/docs and requested
help/ownership overrides remain active. Ordinary creation/explanations need no
full skill, diff, quiz or report.

[Optional Serena setup](serena/README.md) keeps ordinary-tool fallback available.
[Optional Prism continuity](prism/README.md) defaults to a dedicated Mentor database
for explicitly selected project context and requested summary/handoff saves.
The hook and all four workflow context helpers supply its pinned command/guide;
startup performs no Prism calls or writes. The adapter prepares requests for the
primary agent to execute through the selected dedicated connection's exposed tools.
Inspect live host inventory before setup: reuse Serena and compatible dedicated
Prism, including aliases/plugins. Preserve shared Workflow Prism. When requested
connections are missing, [development setup](MCP-SETUP.md) provisions/registers
them through the native host writer. Dedicated Prism uses a Docker volume without
another host port. Missing/incompatible services retain ordinary tools/local docs.
[Original PR #6 evidence](../../docs/evidence/PR6-Prism.md) records earlier reuse
and hook coexistence; [setup/isolation evidence](../../docs/evidence/PR6-MCP-setup.md)
records the subsequent separate-memory request.
[Current evidence](../../docs/evidence/M04-M07.md) records successful native skill
discovery, selected waits/reports, manual compaction, ordinary Python coding and
executable checks. Direct and native-host Serena source calls and the disposable
pinned-SDK DoughTracker build/HTTP checks also passed. The initial routing failures
remain historical receipts. Ordinary help and an explicit review wait also ran
alongside the installed Workflow hooks. The evidence records a nonblocking rewrite
failure and an unnecessary Stop continuation that retained the wait; private
toolkit files were unchanged. New-profile native lifecycle/control, settled
interview invocation, paused review, live PR review and scripted self-check
answer/change handling now have receipts. Model semantic navigation and the
matched build pair record actual tool calls and correct/readable outputs.
See the [acceptance audit](../../docs/evidence/M04-M07-acceptance.md) for original
delivery scope and limits; historical M03 evidence is not a substitute.
