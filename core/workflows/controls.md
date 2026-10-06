# Mentor controls

Level and coaching are separate choices. Unqualified requests affect this session;
only explicit project requests persist. Do not ask a scope question for ordinary
controls. A demonstration, takeover, or more help on a part is transient and does
not change either preference. Explicit authorship agreements always apply.

Use the host-provided control entry and locations. Pass the current conversation's
session object on every call (initially `{}`). The returned session object replaces
that object in conversation context; keep it across resume and compaction. Never
store it in project preferences. Startup/clear begin without previous overrides.
Reloaded project values are defaults, never instructions to discard overrides.
If no control entry is available, session requests can still apply conversationally;
report that project persistence cannot be verified.

| Request | Action / scope |
| --- | --- |
| Use guided, supported, independent | set-level with that value / session |
| Pause or resume coaching | pause or resume / session |
| Show Mentor status | status / session |
| Save a level or coaching choice for this project | corresponding action / project |
| Use project preferences again | use-project / session (all or a requested field) |
| Reset this project's preferences | reset / project |

After a control, apply its effective choices now and retain its session result.
Report session/project scope, effective choices, saved choices when different,
and any warnings. Status refreshes saved defaults while preserving overrides.
When a project write succeeds, only the changed field loses its override. When
it fails, the request still applies as an unsaved local override; say it was not
saved. Do not repair an invalid record without an explicit project reset.
Reset restores guided/on and clears current overrides; a failed reset applies
guided/on as unsaved overrides. Other conversations refresh on status/control
or a lifecycle hook and keep their own overrides. There is no live broadcast.

Guided offers focused coding with context; supported offers coding or reviewing;
independent defaults to agent implementation with learner direction and review.
Paused coaching stops compulsory teaching, while complete readable code, useful
comments/docs, necessary checks, and material defect reporting remain required.
Resume retains the effective level. Do not infer ability or automatically change
levels from a mistake or agent-written code.
