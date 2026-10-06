# M02 — manual levels and project preferences

Status: Implemented and locally verified on 2026-10-06 for the recorded combination.
See [M02 evidence and limitations](../evidence/M02.md), the
[neutral helper contract](../../runtime/README.md), and the
[tested development control guide](../../adapters/codex/README.md).
Native lifecycle/refresh and generated code checks are complete; automatic mid-turn
compaction, broader compatibility and human comprehension remain pending.
Dependency: [M01 foundation](M01-readable-code-core.md).
Contract: [Preferences](../IMPLEMENTATION-PLAN.md#local-preferences) and
[controls](../IMPLEMENTATION-PLAN.md#controls-and-interaction).
Criteria: [T01–T09 and T12 as affected](../TESTING.md#criteria).

## Before and after

Before: a policy-only development hook, guided defaults, and conversation requests
without persistent controls. M01 observed a conversation-only pause surviving
resume/manual compaction, but did not test stored preferences.
After: the learner selects three levels and coaching on/off for the session by
default. Explicit project-scope changes apply now and persist for later sessions.
Session overrides survive resume/manual compaction; clear starts from saved
project preferences. Projects remain separate. Coaching off retains code standards
and defect reporting.

## Scope and precedence

Follow the [operation table](../IMPLEMENTATION-PLAN.md#preference-precedence-and-lifetime).
An unqualified "use independent" or "pause coaching" changes only this session.
"Use independent for this project" or "save coaching off as this project's default"
requests persistence. Do not ask for a scope choice on every control.

Resolve level and coaching separately: session override, otherwise refreshed saved
project value, otherwise guided/on. Status reloads project values without removing
session overrides and displays both when different. A successful project change
clears the corresponding local override and preserves the other saved field and
any override on it. A failed save applies the requested field locally, visibly
unsaved. Demonstration/takeover, task help, and ownership remain separate.

Explicit project reset restores guided/on and clears the current conversation's
overrides. If persistence fails, apply those defaults as unsaved local overrides
and report the failure. Other open conversations refresh project values on
status/control or a lifecycle hook, retaining their own overrides. No broadcast
or automatic preference migration is included.

## Implementation

1. Add a neutral shared state helper and `core/workflows/controls.md`, with a
   thin local host control wrapper only where invocation needs one.
   Keep project resolution, validation, reading, and writing consistent between
   the hook and control path. No external service or private toolkit dependency.
2. Resolve identity from canonical Git common directory, otherwise canonical
   workspace root. Hash it for `<data-root>/projects/<id>/preferences.json`.
   The core accepts explicit data-root inputs; the local adapter maps configured
   `MENTOR_DATA_DIR` or `<user-home>/.mentor` to that contract.
   Same-repo subdirectories/worktrees share settings; separate clones/projects
   do not. Carry the resolved project identity and absolute configured data root
   from hook to controls. Warn on unavailable identity or invalid configuration;
   do not silently choose another record/location. Document non-Git subdirectory
   and moved-project limits.
3. Persist only schema version, exact level enum, and coaching boolean. Missing
   records default guided/on. Invalid/unreadable records warn, use defaults,
   and remain intact until explicit reset. Missing storage retains core policy;
   ordinary mutations refuse to overwrite invalid records and apply the request
   only locally until explicit reset succeeds. Failed writes report non-persistence
   and leave the previous record intact. Session controls/status do not create
   storage. Missing state is a default, not a failure to save.
4. Expose session-default set-level and pause/resume, explicit project mutations,
   status, return-to-project-preferences, and project-only reset. Use atomic
   replacement for writes; preserve the other saved field rather than copying
   a temporary override into it. Report saved/effective values and warnings.
   Document last-completed-write semantics and refresh in already-open sessions.
5. Extend the current policy-only hook with project defaults, persistence warnings,
   and discoverable neutral controls instructions. Label stored settings as
   defaults and retain conversation overrides. Supply trusted resource/helper/
   interpreter locations, project identity, and data root; normal tool calls
   cannot assume hook-only environment variables exist. The thin wrapper uses
   the shared helper, verifies persistence when requested, and applies the result
   to the current conversation. Preference failure preserves the valid policy;
   invalid/missing core policy remains a visible adapter failure.
6. Add level defaults: guided offers focused coding, supported offers coding or
   reviewing, independent defaults to agent implementation with learner direction/
   review. Explicit ownership requests override these defaults. Demonstration/
   takeover and “more help this part” remain transient unless settings are
   explicitly changed.
7. Immediately run state/CLI/hook contracts and the required native lifecycle/
   refresh checks, then S01 under each level and coaching-off plus S03's mistake/
   direct-help case. Use fresh contexts and controlled data. Follow the
   [M02 verification matrix](../TESTING.md#m02-verification-matrix).

No automatic proficiency assessment, evidence ledger, harder-task selection,
new host, marketplace/distribution packaging, or full runner in this slice.

## Immediate acceptance

- [x] T06: all three levels visibly change assistance/participation without
  changing code standards; no coding quota or automatic learner judgment.
- [x] T07: helper/hook round trips preserve explicit settings, project isolation,
  subdirectory/worktree identity, and unaffected saved fields/session overrides.
  Test real temporary roots, canonical/symlink paths, and differing hook/tool cwd.
- [x] T07: session-only controls/status make no storage changes; only explicit
  project mutations persist. Native two-session refresh follows precedence with
  and without a local override; status shows effective/saved settings correctly.
- [x] T08: pause stops compulsory teaching while preserving readable complete code;
  resume retains selected effective level; reset affects only this project's
  preferences and current overrides. Another session keeps its own overrides.
- [x] T08: absent/invalid/unsupported state and failed/read-only storage follow the
  contract; invalid ordinary mutations preserve the record; failed writes/resets
  still apply locally and warn. No destructive fallback or false “saved” claim.
- [x] T03: native startup, resume, manual compaction, and clear pass separately
  with saved state. Resume/compaction retain overrides; clear loads saved settings.
  Automatic mid-turn compaction remains separately pending, outside completion.
- [x] T05/T09: explicit takeover or more-help requests receive useful direct help,
  regardless of level; accepted learner work is verified. Include S03's incorrect
  month-boundary attempt, useful escalation, and corrected-code behavioral checks.
- [x] Rerun T01/T02/T04 where hook/policy changes affect them, and T12 for handback.
  Native evidence includes delivered settings/control guidance and an actual
  control invocation. Handler output alone does not prove these work in the host.

Use the actual local runtime/adapter entry points in focused executable checks. Record host
interaction evidence outside Mentor and update development-hook/control docs with
tested invocation forms. Do not invent custom host slash commands.

## Handback and learning checkpoint

Explain project identity, preference location, hook/control sharing, invalid-state
recovery, and current-conversation versus other-session refresh. Report actual
results and pending checks, supported platforms/versions, and state/concurrency
limits. Record requested/effective/saved choices and session/project scope. Preserve
M01's historical results; do not treat them as passes for the extended M02 adapter.
An agent-written implementation is compatible with independent learner
reasoning during explanation or review.
