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
new root and explicitly set/reset preferences there. There is no migration.

The only saved record is `<data-root>/projects/<id>/preferences.json`:

```json
{"schema_version": 1, "level": "guided", "coaching_enabled": true}
```

Exact fields/types are validated. Missing records use guided/on without creating
storage. Invalid, unsupported or unreadable records stay intact until explicit
reset. Reads and session controls never create storage. An ordinary project
mutation refuses invalid records and applies an unsaved session change. Reset
can replace invalid/unreadable records if the directory is writable.

`control(store, action, scope, value, field, session)` returns requested, effective,
project-default and saved choices; record state, persistence result, warnings,
preference path, and the next session object. `persisted` is true only for a
successful project write/readback, false for a failed project write, and null for
read/session operations. An unavailable store still permits session controls.

For each field, an override wins over refreshed project defaults. Successful
project changes clear only that field's override and preserve the other saved
field. Failed changes retain the requested values as unsaved overrides. Successful
reset clears both current overrides; failed reset overrides both with guided/on.
`use-project` clears all overrides or the selected field without writing.

Session shape (kept in conversation context, never in Mentor's preference record;
the host may persist its conversation transcript):

```json
{"overrides": {"level": "independent"}, "unsaved": []}
```

Every control reloads saved preferences. Other conversations refresh on control
or lifecycle delivery and retain their own overrides. There is no broadcast or
cross-session merge. Writes use a same-directory temporary file, flush/fsync,
atomic replacement and readback. Before-replacement failures leave the prior
record intact; concurrent writes use last-completed-write semantics and may lose
a concurrent field change. A readback mismatch reports persistence as unverified.
This is local preference storage, not a transactional multi-user database.
