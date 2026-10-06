# M02 — manual levels and project preferences

Status: Queued; implementation has not started.
Dependency: [M01 foundation](M01-guided-plugin-foundation.md).
Contract: [Preferences](../IMPLEMENTATION-PLAN.md#local-preferences) and
[controls](../IMPLEMENTATION-PLAN.md#controls-and-interaction).
Criteria: [T01–T09 and T12 as affected](../TESTING.md#criteria).

## Before and after

Before: guided defaults and session requests, without persistent controls.
After: the learner selects three levels and coaching on/off; explicit settings
apply immediately and survive reloads for the same local project. Different
projects remain separate. Coaching off retains code standards and defect reporting.

## Implementation

1. Add a small shared state helper and the bundled `mentor` control skill.
   Keep project resolution, validation, reading, and writing consistent between
   the hook and control path. No external service or private toolkit dependency.
2. Resolve identity from canonical Git common directory, otherwise canonical
   workspace root. Hash it for `PLUGIN_DATA/projects/<id>/preferences.json`.
   Same-repo subdirectories/worktrees share settings; separate clones/projects
   do not. Document non-Git subdirectory and moved-project limits.
3. Persist only schema version, exact level enum, and coaching boolean. Missing
   records default guided/on. Invalid/unreadable records warn, use defaults,
   and remain intact until explicit reset. Missing storage retains core policy;
   failed writes must report non-persistence.
4. Expose set-level, status, pause/resume, and project-only reset operations.
   Preserve the other field on updates; use atomic replacement. Document
   last-completed-write semantics and refresh behavior for already-open sessions.
5. Hook context includes the effective choices and enough trusted resource/data
   location for the control workflow. A normal tool call cannot assume hook-only
   environment variables exist. The skill uses the bundled helper, confirms its
   result, and applies the requested change to the current conversation.
6. Add level defaults: guided offers focused coding, supported offers coding or
   reviewing, independent defaults to agent implementation with learner direction/
   review. Explicit ownership requests override these defaults. Demonstration/
   takeover and “more help this part” remain transient unless settings are
   explicitly changed.
7. Immediately run state/CLI/hook contracts, lifecycle checks, and the same S01
   task under each level and coaching-off. Use fresh contexts and controlled data.

No automatic proficiency assessment, evidence ledger, harder-task selection,
new host, or full evaluation runner in this slice.

## Immediate acceptance

- [ ] T06: all three levels visibly change assistance/participation without
  changing code standards; no coding quota or automatic learner judgment.
- [ ] T07: helper/hook round trips preserve explicit settings, project isolation,
  subdirectory/worktree identity, and unaffected fields. Test real temporary roots.
- [ ] T08: pause stops compulsory teaching while preserving readable complete code;
  resume retains selected level; reset affects only this project's preferences.
- [ ] T08: absent/invalid/unsupported state and failed/read-only storage follow the
  contract; no destructive fallback or false “saved” claim.
- [ ] T03: fresh/resumed/compacted sessions honor saved preferences when exercised.
  Report clear/other lifecycle observations separately; pending is not passed.
- [ ] T05/T09: explicit takeover or more-help requests receive useful direct help,
  regardless of level; accepted learner work is verified.
- [ ] Rerun T01/T02/T04 where hook/policy changes affect them, and T12 for handback.

Use the actual bundled entry points in focused executable checks. Record host
interaction evidence outside Mentor and update installation/control docs with
tested invocation forms. Do not invent custom host slash commands.

## Handback and learning checkpoint

Explain project identity, preference location, hook/control sharing, invalid-state
recovery, and current-conversation versus other-session refresh. Report actual
results and pending checks, supported platforms/versions, and state/concurrency
limits. An agent-written implementation is compatible with independent learner
reasoning during explanation or review.
