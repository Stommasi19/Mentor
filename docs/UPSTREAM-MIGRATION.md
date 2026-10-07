# Agentic Workflow migration assessment and plan

Assessed: 2026-10-07. Status: proposed migration; implementation is not authorized
by this document. The requested work is reviewing the replacement toolkit and
writing this plan. Existing M01–M03 evidence remains historical; M04/M06 remain
unimplemented. Read this alongside the [roadmap](ROADMAP.md),
[M04 handoff](handoffs/M04-review-coaching.md), and [verification criteria](TESTING.md).

## Outcome

Keep Mentor's working core, controls, and interview. Refresh upstream provenance,
make M04's evidence handling more explicit before implementing it, and verify
Mentor alongside the newly installed Codex hooks. Preserve primary-agent teaching,
manual levels, explicit invocation, local artifacts, and report-only review.

The replacement is not evidence that every relevant skill changed. The installed
`withInterview/SKILL.md` is byte-identical to M03's recorded source. The installed
`review/SKILL.md` differs from M04's recorded source, but the removed portable
release is unavailable for a complete comparison. Several useful current upstream
contracts already appear in Mentor's design.

## Source baseline and confidence

The replacement checkout's origin is
[joi-fairshare/agentic-workflow](https://github.com/joi-fairshare/agentic-workflow).
Its clean `main` checkout is at `e0ff305a0f17746858bd63e4752047731edf2282`.
A read-only `git ls-remote origin refs/heads/main` returned that same commit on
2026-10-07. The installed Codex skills and toolkit link resolve to that checkout.
This pins the assessment; it does not promise that upstream will stay at this revision.

Mentor's [attribution record](ATTRIBUTION.md) identifies the previous installation
as `e0ff305-portable-20261006T031059Z`, with a README naming
`vitalizecare/agentic-workflow`. Its commit prefix matches the replacement's HEAD.
Treat this as an installation/provenance change with measured file differences,
rather than assuming a large upstream commit upgrade occurred today.

| Source | Previous recorded SHA-256 | Installed SHA-256 | Conclusion |
| --- | --- | --- | --- |
| `skills/withInterview/SKILL.md` | `f6cc85807ffb378296cf69c6d9b4c4f3d2aef0a0f59e0fc4a7669f293b6ddf11` | `f6cc85807ffb378296cf69c6d9b4c4f3d2aef0a0f59e0fc4a7669f293b6ddf11` | Exact entrypoint match; no source-driven M03 rewrite. |
| `skills/review/SKILL.md` | `2b4d61be25e1110b9cd1ccb7f283dfdd161db12152bd7426dbc60391033062f2` | `25963b307f21f338e59d1def71ea1db77c2b0e37bbfedc0de00e4a3f864e9946` | Confirmed difference; complete old-to-new textual delta unknown. |

The old release/backups directories are empty. Searching the replacement's Git
history for historical review entrypoints did not recover M04's recorded hash.
Do not assign an unverified cause to that difference: it could involve portable
release changes. Matching the interview entrypoint also does not establish that
its shared preamble or dependencies are unchanged.

The analysis below uses three kinds of evidence:

- **Measured replacement difference:** the entrypoint hashes above.
- **Confirmed upstream history:** commits in the replacement repository show when
  particular contracts were introduced, without proving the portable release
  lacked them.
- **Current behavior versus Mentor:** inspected source compared with Mentor's
  implemented workflow or confirmed handoffs. This determines migration needs
  even where an exact historical delta is unavailable.

## Relevant upstream changes and Mentor impact

| Area and inspected source | Current upstream behavior / historical evidence | Effect on Mentor | Migration decision |
| --- | --- | --- | --- |
| `withInterview` | Staged questions, separate delegation round, concrete confirmation, `interview.md`/`plan.md`, target invocation. Entry source matches M03's baseline. | M03 already implements the agreed teaching adaptation, retaining scope/confirmation/artifacts and replacing delegation with participation preferences. | Retain M03; update provenance only. Verify coexistence separately. |
| `review` and `reviewer-prompt.md` | Reads verification `pack.json` and design `comparison-report.json`; missing coverage for a changed user-facing path becomes a blocking finding. Introduced in `1790b97` (#41). | M04 already requires real evidence, accurate pending checks, and scope/revision records. It should explicitly map evidence to changed behavior and distinguish missing proof from a reproduced bug. | Clarify M04's evidence contract; do not require upstream artifact formats or every UI tool. |
| `review` and `triage-prompt.md` | `--lens`, runtime/accessibility concerns for UI changes, named reviewer personas, parallel dispatch. #41 added evidence-aware UI triage; `833d7ae` (#44) clarified host persona fallback. | Concern selection is useful; named agents and dispatch conflict with Mentor's primary-agent workflow. | Apply relevant concerns directly, with proportional scope and no reviewer quota. |
| `review` repeat runs | Saves commit SHA, review-run count, previous finding count and selected lenses; overwrites the PR state file on re-review. #41 added run metadata. | M04 already records revision and prevents silent overwrite. Commit SHA alone does not identify dirty local work. | Preserve each task report; identify local snapshots and stale evidence. Run counters are optional. |
| `review` investigation handoff | Offers up to three parallel `rootCause` runs for traced findings. `rootCause` can investigate and implement a fix unless restricted. | M04 ends at findings. Entering another workflow can broaden scope or edit code. | Describe a next investigation when useful; invoke nothing automatically. A separate request defines its scope. |
| Shared preamble and capabilities | `833d7ae` moved repeated boilerplate into `_preamble.md` and made capability language/provider roles portable. The preamble still includes toolkit setup, Prism context loading and session saves. | Mentor already has a neutral core/thin Codex adapter. Importing the preamble would add private installation and service dependencies. | Retain Mentor's own context helper and capability handling; do not copy or depend on the toolkit preamble. |
| Shared plan layout/discovery | Defines `plan.md`, optional product/engineering/design/task artifacts, reader matrices, and newest-plan discovery. | M03's two files are sufficient for its own contract. Upstream consumers discover a different data root and can expect additional documents. | Pass explicit artifact paths. Do not assume upstream auto-discovery reads Mentor's plans or generate an entire planning suite for every task. |
| `archReview` / `productReview` | Concrete file evidence, boundary analysis, normalized severity/verdicts, explicit coverage; also diagram counts, matrix requirements, scores, forced cuts and deadlines. | These are future inspiration in `DESIGN.md`, not current Mentor runtime features. Mentor already rejects disproportionate quotas/scores. | Retain evidence-backed reasoning; defer new lenses until the first local version is exercised. No migration milestone for them now. |
| `specToProvenPR` | `e0ff305` (#64) emphasizes use in the running app before review, then final-code rechecks. It also requires evidence packs, a zero-findings loop, publication steps and additional skills. | Mentor already requires immediate slice verification and actual hook/skill delivery. Zero optional findings and automatic ship orchestration conflict with Mentor's scope and polish distinction. | Carry forward relevant real-entrypoint checks and evidence freshness. Keep PR/deploy orchestration outside Mentor's review skill. |
| `testAudit` | Authoring gate, focused audit and campaign modes; meaningful behavioral contracts over implementation/prose assertions. Has its own OpenClaw MIT attribution notice. | Aligns with Mentor's testing criteria and prior development use. It is not a core/runtime dependency. | Use its appropriate development mode when tests are changed; do not add audit campaigns to this migration. |
| `ui-evidence` / `bugFixOrchestrator` | Real UI actions and provenance, specialized planning/repair, model/judge helpers, locks, ticket publishing; bug orchestration requires delegation. | Useful evidence ideas, but substantial new integrations and incompatible primary-agent targets. Mentor currently has no web UI requiring this pipeline. | Defer integrations; accept relevant supplied evidence with provenance. Do not make either skill a first-use dependency. |
| Installed Codex hooks | User hooks now include SessionStart context/health, prompt sorting, scope/external-write gates, context guard and Stop done-gate. | Earlier isolated Mentor evidence does not certify this combined installation. Hook presence does not prove delivery or a conflict. | Run focused native coexistence checks; keep runtime protocols in adapters. |

Pinned sources for these decisions:
[review](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/skills/review/SKILL.md),
[evidence pack](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/skills/_shared/evidence-pack.md),
[plan layout](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/skills/_shared/plan-layout.md),
[capabilities](https://github.com/joi-fairshare/agentic-workflow/blob/e0ff305a0f17746858bd63e4752047731edf2282/skills/_shared/capabilities.md),
[#41 contracts](https://github.com/joi-fairshare/agentic-workflow/commit/1790b97608a03c7a7a3d139fc580365d0e0c2a7c),
[#44 shared preamble/provider changes](https://github.com/joi-fairshare/agentic-workflow/commit/833d7ae7adde2b15a4ad841e90f064f17f73f3eb),
[#64 function-before-review changes](https://github.com/joi-fairshare/agentic-workflow/commit/e0ff305a0f17746858bd63e4752047731edf2282).

## Proposed M04 evidence contract

Keep M04's existing sequence: target/context → concerns → learner primer → pause
or skip → evidence-backed discussion → local report. These additions clarify
the evidence used by that sequence; they do not start implementation or replace
the confirmed learner experience.

1. **Identify the reviewed change.** For a PR, record repository, base and head
   revisions. For local changes, record base/HEAD plus included staged, unstaged
   and untracked content. Use a retained diff/content digest or equivalent snapshot
   identity when needed; HEAD alone cannot identify an uncommitted change.
2. **Connect evidence to behavior.** For each relevant changed flow or public
   contract, state which available check covers it, its result and its provenance.
   Inspect the actual results. An available file or a general PASS label does not
   establish that this flow was exercised.
3. **Use project-appropriate proof.** CLI/API output, contract tests, host receipts,
   browser/simulator journeys and design comparisons can all be relevant. A UI
   change warrants relevant runtime/accessibility evidence; a neutral helper or
   document does not acquire a screenshot requirement. No mandatory `pack.json`,
   UI service, lens count or end-to-end runner is introduced.
4. **Check freshness.** Use evidence tied to the reviewed revision/snapshot and
   relevant configuration when known. The newest directory may concern another
   feature or an older change. Unknown provenance is unknown. Recheck affected
   evidence when code changes during the learner pause or a separately requested
   fix; preserve valid unrelated evidence.
5. **Separate defects and verification gaps.** A reproduced defect gets location,
   trigger, consequence and supporting evidence. A missing required check gets
   the uncovered behavior, why that check is required and a concrete next check.
   Missing proof does not prove defective behavior. An unrelated optional evidence
   pack is not a blocker merely because upstream uses one.
6. **Save truthful reports.** Include scope/snapshot, findings, relevant checks,
   evidence references, limitations and optional refinements. Prefer references
   to evidence over copied conversation history. Preserve previous reports; do
   not collect learner scores, full transcripts or a progression ledger.

For example, if an interview artifact helper changes, its relevant evidence is
directory isolation, collision/failure behavior and an actual host invocation.
A browser screenshot adds no useful proof. If a reviewed PR changes a form,
a general build PASS leaves submit/error behavior unverified until a relevant
check covers it. Both cases should remain understandable in the report.

M06 can reuse the same distinction between current evidence, unknowns and pending
checks when it is implemented. It still gives immediate feedback without requiring
a learner reflection or silently launching M04.

## Migration steps

### Step 1 — reconcile references and agree the M04 clarification

Proposed files: `docs/ATTRIBUTION.md`, `docs/handoffs/M04-review-coaching.md`,
`docs/TESTING.md`; update `docs/DESIGN.md`/`docs/IMPLEMENTATION-PLAN.md` only where
the clarification changes their contracts. Link this assessment from
`README.md`/`docs/ROADMAP.md` when adopting it.

- Preserve previous provenance and source hashes as historical records. Append
  the replacement repository, full commit, current hashes and comparison limits.
- Add the evidence contract above and applicable cases to M04's handoff/matrix.
  Keep its status planned and all runtime acceptance rows pending.
- Record inspected terms: no repository-wide LICENSE was found in the tracked
  replacement files; `skills/testAudit/NOTICE.md` applies to that adaptation.
  It does not settle copying permissions for other skills. Use originally authored
  Mentor instructions; verify relevant terms/notices before any source copying.
- Retain M03's completed status. There is no measured entrypoint change requiring
  a rewrite; any later demonstrated defect gets a separate scoped correction.

Done when the documents agree, relative links resolve, and historical/runtime
claims remain accurate. This step is documentation work; no runtime pass is claimed.

### Step 2 — implement M04 as the next focused product slice

After a separate implementation request and agreement on the slice, use the
revised M04 handoff to add `core/workflows/review.md`, a thin Codex native wrapper,
and only the neutral report handling needed. `InterviewArtifacts` currently
handles interview/plan files; a review report must not misuse its confirmation
semantics or require an interview. Reuse validated project/data-root handling
without widening the preference schema.

Use M02's current session overrides and refreshed defaults without writes.
Resolve local/PR scope through the adapter, save separate reports, and perform
the primer/pause/skip/report behavior through the primary agent. Evidence mapping
can start as clear report content; no generalized evidence ingestion framework,
upstream JSON compatibility layer or full evaluation runner is required.

Verify every existing M04 acceptance row plus the additions below immediately.
Record actual native invocation, software checks and conduct separately. A saved
workflow file alone is not completion.

### Step 3 — verify the updated development environment

Run this focused probe before relying on Mentor in the combined installation;
M01–M03 can be probed before M04 exists. Use a disposable external workspace and
the host's normal hook trust/review flow. Preserve user hook files and preferences;
do not reinstall upstream or disable global controls to force a pass.

Compare an isolated Mentor run with one using the current installed toolkit
hooks. Record the Codex version, model, target language, registered hooks/skills,
and receipts/transcript evidence. Exercise ordinary work, explicit interview,
requirements-only completion, confirmation/learner waits, manual controls and
coaching-off. Add M04's native review/pause/report after its implementation.

If a prompt/Stop hook continues a deliberate learner wait, changes the task scope,
or prevents a truthful scoped handback, record the actual conflict and identify
the responsible hook. Configuration presence alone is not a failure. Resolve an
observed conflict within an agreed slice; do not silently patch the personal
toolkit or change Mentor's learning contract.

Done when the exercised combination has real delivery/conduct evidence, including
intentional waits, and any untested combinations or unresolved conflicts are
explicit. Preserve earlier isolated reports without relabeling them.

### Step 4 — continue the existing roadmap

Proceed with [M05 portability and optional Serena tooling](handoffs/M05-portability-and-tooling.md)
and the [M06 feedback and optional PR understanding-check plan](handoffs/M06-task-feedback.md).
M05 already pins the replacement upstream revision for Serena; retain its
repository-owned setup, existing-connection reuse, fallback and no-memory requirements.
Keep the PR self-check separate and explicitly invoked, with its own answer/wait
sequence; ordinary feedback still has no quiz prerequisite. Carry the evidence
distinctions into both workflows' reports. Architecture/product lenses, UI-specific
integrations, general upstream handoff interoperability and full evaluation
automation remain optional future work. M08 remains the final packaging and
distribution phase; this migration adds no installer or public release.

## Verification additions for the proposed slices

These are planned observations, not checks performed during this assessment.
Use meaningful process tests for storage/entrypoint boundaries and native
transcripts for agent conduct; avoid exact-wording assertions and mirrored tests.

| Case | Expected observation | Relevant criteria |
| --- | --- | --- |
| Matching evidence | A result for the reviewed snapshot and changed flow supports the report's claim; supplied evidence is inspected. | T11/T12 |
| Newest but unrelated evidence | A newer pack for another feature is not used as proof; the uncovered check remains pending. | T11/T12 |
| Stale or unknown provenance | Old/untied results are labeled accurately; no current PASS is invented. | T11/T12 |
| Dirty local change | Report scope identifies staged/unstaged/untracked content; equal HEADs with different content are not treated as identical snapshots. | T11/T12 |
| Change during learner pause | Refresh affected scope/evidence and identify stale observations before finalizing. | T11/T12 |
| Missing required check | Report a concrete verification gap and next check, without inventing a code defect or mandatory upstream format. | T11/T12 |
| Non-UI work | Relevant helper/CLI/API/document checks suffice; no screenshot or private UI stack is required. | T12/T13 |
| Real defect plus optional polish | Report every identified material defect with evidence; refinements remain optional and serious findings are disclosed immediately. | T11/T12 |
| Repeat/save failure | Preserve previous reports, handle directory collisions and surface failed/partial persistence without a success claim. | T11/T12 |
| Report-only scope | Review edits no implementation, posts nothing and invokes no debugging/fixing workflow. | T11/T12 |
| Combined host behavior | Actual hook/skill receipts show delivery; ordinary work does not implicitly activate full skills, and deliberate waits remain waits. | T01–T03/T10–T13 |
| Manual preferences and feedback | Levels/session overrides remain intact; agent-written proof establishes no human learning or automatic progression. | T06–T08/T12/T15 |

When runtime work is authorized, run applicable existing checks
(`python3 -m unittest discover -s tests -v`), meaningful new boundary checks, and
the relevant native host scenarios. Broaden checks only for changed contracts or
unresolved failures. The unfinished fixture starter is not a passing candidate.

## Source fingerprints for future refreshes

All paths below are relative to the pinned upstream checkout. These fingerprints
make a later replacement comparable even if its installation layout changes.

| Inspected source | SHA-256 |
| --- | --- |
| `skills/review/reviewer-prompt.md` | `8e1ea89797a742fffe13f804e720d92dc1662637fbe01d6cc1b2b0ad4deffaa5` |
| `skills/review/triage-prompt.md` | `82246b09b7c4eb8b208c8ae1d94a00d9587642edf1af65aa068f409684de85e1` |
| `skills/archReview/SKILL.md` | `91b261bb263b3717defbe2405e45a39152b6b257699f1c577e047bfba312906a` |
| `skills/productReview/SKILL.md` | `ea3b59a72367e8779ecfbbe86389e94e7ad312aa29fc34c15b2ed055424c9169` |
| `skills/_preamble.md` | `5a32cd5aa9b424c0ba11df8e5fd8db9aa4b03f2f3e2502f02b484c8f7a429068` |
| `skills/_shared/capabilities.md` | `c4516f7e70f50689806583c0b91361dd9924c3573287d690f5b65762ea5be672` |
| `skills/_shared/evidence-pack.md` | `8876d7e4cff2ac3942b98ec83c1dfdbf4a7c571c9789719fba9977c531fbb25d` |
| `skills/_shared/plan-layout.md` | `8b51446bc52bf8d2fc3a82d1128b71b72e978f7e61a5779845811b08e86ca336` |
| `skills/specToProvenPR/SKILL.md` | `29485e140862225174578c1c8e45ad2ca4066df7ee3692e9180dec0782deeef7` |

For the next refresh, first resolve the installed source and its clean/dirty state,
record commit and hashes, then compare changed entrypoints and referenced files.
Map each difference to an implemented contract, planned slice or deferred idea.
Avoid copying the entire upstream skill set into Mentor or changing contracts
merely because a toolkit file changed.

## Work completed and remaining

Completed in this assessment: source/remote verification, installed-link and hook
inventory, recorded-hash comparison, relevant source/history inspection, comparison
with Mentor's core/M03 and M04/M06 plans, and this proposed migration document.
Upstream skill files were read as source material, not invoked as workflows.
No source text/templates were copied into Mentor's implementation.

Pending: adopting the proposed document changes, M04 implementation, runtime
coexistence/native checks, broader compatibility and any human-learning evidence.
No runtime tests or hook experiments were run for this documentation task, and
no upstream, personal hook configuration, Mentor runtime or preferences were changed.
