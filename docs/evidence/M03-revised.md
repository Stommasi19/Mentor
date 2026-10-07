# Revised M03 verification — 2026-10-07

Status: **local pass for the revised skill contract and recorded combination**.
[Original M03 evidence](M03.md) remains historical. This report covers the native
explicit-only skill, staged teaching interview, confirmed local artifacts, and
primary-agent continuation. Scripted conversations do not establish human learning.

## Implementation and environment

The canonical `core/workflows/interview.md` follows the confirmed M03 sequence
with original wording. The core policy permits ordinary clarification but no
automatic full interview. The thin Codex skill wrapper resolves the real checkout,
reads effective/saved M02 status with the retained session object, and loads the
canonical policy/workflow. Native metadata sets `allow_implicit_invocation: false`.
The hook advertises the skill without registering or loading its body.

`runtime/artifacts.py` reserves separate local task directories, appends the
interview record, and writes the confirmed plan. Its Codex entry receives explicit
root/project locations. It does not write preferences or choose a fallback root.
Failed writes produce no success result; partial finalization is documented and
requires inspection/recovery before continuation. See [usage](../../adapters/codex/README.md),
[storage contracts](../../runtime/README.md), and [attribution](../ATTRIBUTION.md).

| Component | Recorded value |
| --- | --- |
| Host / provider / model | Codex CLI/native app-server 0.160.1; OpenAI `gpt-6.1-sol`, medium reasoning, fast tier |
| Runtime / coding fixture | macOS arm64; Python 3.14.3 standard-library helpers; C#/.NET 9, SDK 9.0.304 |
| Native registration | Repository `.agents/skills/mentor-interview` symlink to the development adapter; actual `skills/list` reports enabled repo scope and no load errors |
| Invocation | Native `turn/start` skill input with the registered name/path, as used by a skill selector; full wrapper injected by the host, canonical workflow read by actual commands |
| Isolation | Disposable external workspaces; project-document loading, unrelated skills, plugins/apps/MCP, web search, and multi-agent disabled; no pasted Mentor developer prompt |
| State | Explicit experiment data root; controlled guided/on saved defaults; supported, independent, and pause chosen for the session only |
| Authorship | Scripted user replies; primary agent authored generated code/docs/artifacts. No independent human exercise or learner assessment |

Raw evidence lives outside public Git at
`~/.local/share/mentor/experiments/2026-10-07-m03-revised/`. It includes command/input
records, native events, thread snapshots, rollout copies, preference/source
snapshots, actual Markdown artifacts, generated candidate, and check outputs.
`manifest.json` indexes the evidence; `runtime-sha256.json` records tested runtime
resources. The one-off observer scripts are evidence aids, not a product runner,
subagent workflow, or runtime dependency. Shared filesystem access makes these
development simulations, not isolated actor studies.

## Acceptance results

| Criterion | Result | Evidence |
| --- | --- | --- |
| Native invocation and ordinary-task control — T10/T12/T13 | pass locally | `s02-skills.json` records registration; `s02-turn1.jsonl` has native skill input and actual workflow read; `s02-rollout.jsonl` has the injected wrapper. Ordinary task has no skill block/body, workflow read, commands, or new plans, while ordinary clarification still works. |
| Affected startup delivery — T01/T02 | pass for exercised events | Normal CLI folder/hook review and trust flow, recorded in `trust-ui-notes.json`. Five completed native hook receipts across S02 startup/resumes and the ordinary control; canonical policy visible in both rollouts. Process tests retain startup/resume/clear/compact and invalid-resource coverage. |
| Stages, decisions, and teaching — T06/T10 | pass in simulation | Guided S02 turns 1–3 retain target/time box, focused questions, known participation preferences, boundary drill-down/example, assumptions, checks and concrete confirmation. Supported and independent runs demonstrate brief tradeoff support and concise decisions. No subagent use, exercises, grading, or inferred level changes. |
| Pacing and paused coaching — T08/T10 | pass in simulation | Paused and handoff settled/skip inputs reuse exact prior approvals, save/read both artifacts and finish without invented rounds or another gate. Paused retains requirements/artifacts while applying only the explicitly requested session pause. |
| Confirmation and scope — T10 | pass in simulation | S02 source snapshots remain identical before turn 4 approval. Turn 4 finalizes/readbacks artifacts before implementation, then completes checks without another gate. Supported, independent, paused, missing-target recovery and failure recovery leave source unchanged; requirements-only code checks remain pending. |
| Artifacts and handoff — T10/T12 | pass locally | Actual Markdown records preserve scope, questions/answers, assumptions, confirmation and checks. Handoff target receives original request, verbatim constraint, both references; its real entrypoint is read and followed by the primary agent. Missing target waits for a chosen replacement. Real blocked plans path stops handoff, then recovers at the same root. CLI tests independently cover collisions, partial write failure, recovery and invalid directory/configuration. |
| Resulting software — T04/T12 | pass for one generated candidate | S02 candidate passes 9 base and 11 including reserved independent fixture checks. Agent's separate build/check harness passes 120,005 assertions, including all 119,988 representable months. Actual code/comments/README inspected separately. |
| Neutral boundary and claims — T12/T13 | pass for inspected architecture and evidence | Canonical workflow/storage have no learner-language, vendor/model, host API, private-toolkit or service dependency. Host metadata/env/quoting stay in the adapter. Only this combination is verified; other compatibility and human-learning claims remain pending. |

All 13 executable contract tests pass in `unit-checks.txt`; four new interview tests
protect the real context/artifact process boundaries without test-only seams.
`test-authoring-gate.md` records behavior, credible regression, distinct coverage,
and seam assessment. Skill Creator's validator passes using an external temporary
venv for its PyYAML dependency; the product uses no PyYAML. `git diff --check` passes.

## Conversation observations and recovery

- **Guided S02, turns 1–4:** Turn 1 records the original request, "30 min" and
  calculation-only scope, reuses matching/date/decimal answers and worked-example
  ownership preferences, and asks only refunds and boundaries. Turn 2 responds to
  the supplied boundary misconception with a single November 1 expense counted
  twice. Turn 3 records the chosen rule, December 9999 approach and explicit
  assumptions, then pauses for concrete-plan confirmation. Turn 4 captures actual
  approval, finalizes and reads both files, implements and checks the agreed task.
  No preference record is created. The simulation's acknowledgement is not proof
  of unaided human understanding.
- **Supported / independent, turns 1–3:** The same essential monthly net-spending
  decision is exercised under explicitly selected session levels, while saved
  guided/on stays unchanged. The supported response compares the existing one-value
  API with separate gross/refund values; independent uses a concise options table.
  User teaching preferences also differ, so this is observed contract conduct,
  not a controlled causal measurement of the level alone. After plan confirmation,
  both records are saved/read back without implementation or a second gate.
- **Read-only resume recovery:** The first observer resumes for supported and
  independent omitted explicit sandbox selection and the host chose read-only.
  Both sessions reported that the latest answers/summary were unsaved rather than
  inventing persisted success. The observer restored explicit workspace-write on
  resume; turn 3 records confirmation and persists the missing entries/plan.
  The failed attempts remain in the traces. This is a harness configuration recovery,
  not an artifact failure hidden by a pass.
- **Paused settled/skip, one turn:** Uses the exact plan already approved in the
  input, applies the requested session-only pause, and saves/readbacks the two
  artifacts with pending code checks. Saved guided/on and source stay unchanged.
  No requirement to resume coaching, teaching prompt, or compulsory exercise.
- **Selected handoff, one turn:** After both saved files are read, the primary agent
  explicitly announces and reads the available local `mentor-test-target` entrypoint,
  follows it and writes `HANDOFF.md`. That document retains the original request,
  exact "--slim 5 min; requirements only, no UI, no implementation" constraint and
  both references. It accurately marks implementation/checks pending.
- **Missing target, two turns:** Reports `mentor-does-not-exist` unavailable, records
  the unresolved target, and does not silently implement. After the user chooses
  requirements-only and approves its concrete plan, records the replacement and
  saves/readbacks both files. Preferences/source remain unchanged.
- **Blocked artifacts, two turns:** A real file at the project's `plans` path makes
  directory creation fail. The agent reports no saved interview/plan and stops
  before handoff without substituting storage. After the observer removes the
  blocker, it retries the same root, preserves existing approval, saves/readbacks
  both artifacts and leaves code/checks untouched.
- **Ordinary task, one turn:** Native hook policy loads, but the explicit-only wrapper
  is absent from the rollout. The response explains exclusive month boundaries;
  no command, workflow read, artifact, preference write or code edit occurs.

## Code, comments, and documentation review

The candidate keeps the public API and uses a descriptive `total` with a direct
single-pass loop. `StringComparison.OrdinalIgnoreCase` preserves culture-neutral
matching without trimming. Comparing year/month implements the chosen calendar
boundary and avoids constructing January 10000; the in-code comment explains
that non-obvious rule. Public XML docs cover refund signs/negative results,
matching, ignored day, valid-input assumptions, zero results and intermediate
`decimal` overflow. The README supplies a signed-refund example, significant
whitespace behavior, date limits and runnable checks. No unfinished placeholder
remains. The accumulation does not mutate records or the input collection.

Independent observer checks include decimal precision, culture-independent
matching, boundary exclusion and reserved date-limit cases. The first run covered
9 checks; a later explicit `--reserved` run covered all 11. These outcomes are
recorded separately rather than attributing unrun reserved cases to the first run.
Readable-code observations and passing behavior do not establish a causal quality
improvement over a baseline or human learning.

## Limits and next task

The disposable test hook was left disabled through the ordinary `/hooks` UI
after verification; no global hook or public installation was added.

Native evidence covers explicit selector-style skill input, startup/resume policy
receipts and this registered Codex development wrapper. It does not certify every
host's textual mention parser or another host's registration metadata. Clear and
compact remain process coverage for this revision; M02's native lifecycle results
are historical. Automatic mid-turn compaction, broader languages/models/providers,
Windows and unaided human learning remain pending. Full evaluation automation,
review/task-feedback implementation, packaging and public installation/release
remain later work. M04 is the next implementation slice.
