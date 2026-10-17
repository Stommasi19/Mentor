# Neutral preference helper

`preferences.py` uses Python's standard library. It has no host schema, environment
configuration, model/provider API, or target coding-language defaults. Hosts supply
an absolute data root, a resolved project ID, and the current conversation's session
object. `resolve_project(workspace)` hashes the canonical Git common directory
with SHA-256; outside Git it hashes the canonical workspace directory. Git must be
available; a failed lookup disables persistence rather than selecting a new identity.

Repository subdirectories, symlinks and linked worktrees share settings. Separate
clones do not. Start non-Git projects at their root: nested starting directories
are distinct identities. Moving a project can change its identity; select the
new root and explicitly set/reset preferences there. There is no automatic
relocation of saved project records.

The only saved record is `<data-root>/projects/<id>/preferences.json`:

```json
{"schema_version": 2, "level": "junior", "coaching_enabled": true}
```

Exact fields/types are validated. Missing records use junior/on without creating
storage. Invalid, unsupported or unreadable records stay intact until explicit
reset. Reads and session controls never create storage. An ordinary project
mutation refuses invalid records and applies an unsaved session change. Reset
can replace invalid/unreadable records if the directory is writable.

Canonical levels are `junior`, `mid-level` and `senior`. A valid version-1 record
uses `guided`, `supported` or `independent`; reads translate those choices to the
corresponding canonical level without rewriting the file. Retained legacy session
overrides and explicitly supplied aliases translate the same way. Status includes
legacy metadata so the translation is visible. Only an explicit project mutation
or reset writes version 2. Unknown versions or invalid combinations remain invalid;
they never silently revert to defaults or migrate on read.

`control(store, action, scope, value, field, session)` returns requested, effective,
project-default and saved choices; record state, persistence result, warnings,
preference path, and the next session object. `persisted` is true only for a
successful project write/readback, false for a failed project write, and null for
read/session operations. An unavailable store still permits session controls.

For each field, an override wins over refreshed project defaults. Successful
project changes clear only that field's override and preserve the other saved
field. Failed changes retain the requested values as unsaved overrides. Successful
reset clears both current overrides; failed reset overrides both with junior/on.
`use-project` clears all overrides or the selected field without writing.

Session shape (kept in conversation context, never in Mentor's preference record;
the host may persist its conversation transcript):

```json
{"overrides": {"level": "senior"}, "unsaved": []}
```

Every control reloads saved preferences. Other conversations refresh on control
or lifecycle delivery and retain their own overrides. There is no broadcast or
cross-session merge. Writes use a same-directory temporary file, flush/fsync,
atomic replacement and readback. Before-replacement failures leave the prior
record intact; concurrent writes use last-completed-write semantics and may lose
a concurrent field change. A readback mismatch reports persistence as unverified.
This is local preference storage, not a transactional multi-user database.

## Interview artifacts (M03)

`InterviewArtifacts` uses the same explicit canonical data root and 64-character
project ID as preferences. It reserves
`<data-root>/projects/<project-id>/plans/<local-date>-<task-slug>/` with exclusive
mkdir and numeric collision suffixes, then creates `interview.md`. Non-Latin
labels use a safe fallback slug. Existing interviews are never reused by `create`.
Startup/status/context resolution does not create plan directories.

`append` preserves earlier Markdown entries. `finalize` requires nonempty
confirmation and plan text, appends the confirmation, and writes `plan.md`.
Confirmation text records an actual user approval; the helper cannot determine
whether the user approved the plan. The workflow must verify that separately.
Directory operations accept only absolute task directories belonging to this
project's plans. The helper never writes preferences or chooses a fallback root.

Errors remain visible and the adapter emits no successful result. The two files
are not a transaction: a failed finalization can leave a confirmation entry or
partial plan. Inspect and repair the record, retry, and read both files back
before execution/handoff. Concurrent interviews reserve separate directories;
concurrent writers to the same interview are unsupported. Retention/deletion is
manual for this local prototype. There is no learner profile or background ledger.

## Task reports (M04–M07)

`reports.py` takes an explicit canonical data root, project ID and report kind.
`review`, `feedback` and `pr-check` reserve directories under `reviews`, `feedback`
and `pr-checks`, respectively. Each reservation uses the local date and a bounded
task slug, with exclusive mkdir and numeric collision suffixes. Its ownership
marker allows a separate save process to validate the same project and category.
Reads/context resolution do not reserve reports or alter preferences.

`save` accepts nonempty Markdown and publishes `review.md`, `feedback.md` or
`pr-check.md`. It flushes/fsyncs a same-directory temporary file, links the complete
file exclusively into place and reads it back. An existing report is never
overwritten, including concurrent saves. Filesystems without hard-link support
fail visibly; there is no less-safe replacement fallback. A failure after publication
can leave the report present even though verification failed; inspect that file
before reserving a retry. Directory durability across sudden power loss is not
guaranteed.

Paths must belong to the reserved project/category; symlink redirects below the
resolved data root are rejected. Storage errors remain visible with no successful
result or fallback root. This local helper stores task reports, not an ability
grade, automatic level change or background learner ledger. Report content must
distinguish agent assistance, independently supplied learner reasoning, actual
checks, simulations and pending observations; the filesystem cannot establish
those facts itself. Retention/deletion remains manual.
