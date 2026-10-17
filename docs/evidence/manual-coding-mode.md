# Manual coding mode — 2026-10-17

PR #6 subsequently merged without this change. It is now carried on the
main-based private-use follow-up branch; see [private package checks](private-plugin.md).
The attempted publication below is retained as historical evidence.

Implemented following the user's request for a persistent option to write all
code with insightful guidance and review. Existing uncommitted M04–M07 work was
preserved. At the user's subsequent request, PR #6 integration was prepared in an
isolated clone based on `578f0eaf6fb715850224481ac0782b87d427e2dc`, retaining its
separate Prism storage and missing-tool setup. No external project implementation
or real learner preference was changed.

## Implementation

- `runtime/preferences.py`: independent `coding_mode` enum (`manual`, `assisted`),
  session/project controls, field-specific refresh, atomic save/readback and schema
  3. Valid schema-1/2 records retain assisted behavior without a rewrite. Invalid
  records remain intact until explicit reset. Level and coaching never switch
  ownership; explicit project changes preserve the other saved fields.
- Codex control and lifecycle handler: expose `set-coding-mode manual|assisted`
  and `--field coding_mode use-project`, deliver the current project mode, retain
  existing session precedence and distinguish saved from effective values.
- Core/controls/interview: manual means inspect, explain, offer progressive hints,
  review and requested non-destructive checks. No implementation edits or complete
  task solution without a scoped explicit request. Feature requests and plan
  confirmations in manual mode guide learner work. Demonstrations/takeovers do
  not change saved mode; guidance resumes afterward. Requested plans/reports
  remain allowed. Paused coaching preserves manual ownership.
- Usage and state documentation explain the setting, backwards compatibility,
  reset, failure behavior and the difference from host filesystem permissions.

## Executed checks

Final command, using Python 3.14 on this macOS checkout:

```text
python3 -m unittest discover -s tests -v
Ran 28 tests in 15.427s
OK
```

No tests skipped. Python AST parsing of all runtime/adapter/test files passed;
`git diff --check` passed; all 233 relative Markdown file links resolved.
The suite includes actual subprocess control calls,
filesystem preferences, lifecycle-handler execution, relocated skill wrappers,
and real non-root permission failures. These are process-boundary checks, not a
native host/model conversation.

New coding-mode tests were run before implementation: both failed because the
actual CLI rejected `set-coding-mode` (exit 2). They passed after implementation.
The final suite also verifies default compatibility, records from both older
schemas, invalid new values/records, reset and unsaved failed requests.

A separate retained receipt executed the actual shell-quoted control command
supplied by the handler against a disposable project/data directory. Saving manual
mode returned:

```json
{"effective":{"level":"junior","coaching_enabled":true,"coding_mode":"manual"},"saved":{"level":"junior","coaching_enabled":true,"coding_mode":"manual"},"persisted":true}
```

A fresh status process returned the same effective/saved choices with
`persisted:null` (read only). This did not enable manual mode in a real project.
Source inspection confirmed simple enum validation, read-only old-record defaulting,
field-specific mutation and intent comments; no target-language/model dependency
or test-only production seam was introduced.

## Test authoring gate

| Owner / verdict | Observable contract and credible regression | Coverage gap and production boundary |
| --- | --- | --- |
| New manual-project test — pass | Actual saved mode remains manual across every level, pause/resume and all four lifecycle handler sources; another project stays assisted. A dropped field or profile-coupled ownership fails. | Existing tests had no coding ownership control. Uses actual control/handler processes and records, with no mocked persistence or test-only seam. |
| New session/refresh/failure test — pass | Temporary assisted mode does not write or leak into a level save; saved manual is restored by field refresh/clear; failed save remains an unsaved manual choice; reset restores defaults. Session-flattening or false persistence fails. | New mode precedence is distinct from existing level/coaching choices. Same actual CLI owner boundary; no new production hook for tests. |
| Existing migration/rejection/default tests — pass | Old records stay byte-identical on reads; explicit writes publish schema 3; missing/invalid enum fields reject without writes. New record strictness and changed-schema handling could regress independently. | Extends existing owners rather than duplicating tests. New mode validation is exercised through real CLI/handler behavior. |
| Existing interview/three workflow wrapper tests — pass | Manual session overrides survive interview context, and saved manual mode reaches review/feedback/PR-check after relocation without preference writes. Adapter state filtering could drop the new field even when the core works. | Distinct adapter transport risk not reached by core control tests. Executes real wrapper entry points, not source-string assertions. |
| Existing adapter command test — pass | An unrelated working directory executes the delivered command and obtains all three defaults. | Updates the existing public serialized result expectation; no duplicate test added. |

Raw logs, saved/fresh status receipts, initial failures, handler output and an
incremental patch against the pre-existing working files are retained locally in
`/private/tmp/mentor-manual-mode-799m_xbs/`. Temporary artifacts may be removed by
the operating system; the checked results and limits above are retained here.

## PR #6 integration checks

The isolated PR clone retained the newer Prism/Serena integration and applied only
this manual-mode delta. Its full combined suite ran after resolving the wrapper
patch against the newer Prism assertions:

```text
python3 -m unittest discover -s tests -v
Ran 35 tests in 18.510s
OK
```

No tests skipped. Python syntax and `git diff --check` passed, and 268 relative
Markdown file links resolved. The original 28-test result above remains scoped to
the working checkout before PR integration. PR receipts are retained locally under
`/private/tmp/mentor-pr6-manual-zv37sswz/`. These integration checks add no new
native model or human-learning observation.

## Earlier attempted publication

The user explicitly requested adding this change to PR #6. The existing PR head
was verified through GitHub as `578f0eaf6fb715850224481ac0782b87d427e2dc`.
Normal Git transport failed DNS resolution in this session. The connected GitHub
write tool rejected creation of the new tree with: “MCP tool call requires approval,
but approval policy is never”. No remote commit or branch update occurred.
The isolated clone contains the tested change, prepared for a normal fast-forward
publication when an approved write connection is available. That attempt left
PR #6 unchanged; the subsequent merge did not include manual mode.

## Pending observations

No fresh native host/model session was run for this revision. Automatic delivery,
manual guidance/review with unchanged learner source, a scoped requested
demonstration and return to manual behavior remain unobserved for this change.
Passing persistence/handler tests does not prove a model obeys the no-edit policy.
The mode does not revoke filesystem/tool permissions. No human contribution,
understanding or learning result is claimed, and historical native evidence is
not relabeled as proof of this new mode.
