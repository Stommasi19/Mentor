# M04 — explicitly invoked review skill with learner priming

Status: Implementation explicitly requested and performed on 2026-10-07.
[Boundary and S04 checks pass at their stated scope](../evidence/M04.md); native
conduct checks are recorded for local and PR targets, primers/waits/direct/paused
findings and report-only behavior. Planning approval alone does not authorize implementation.
Dependency: [Revised M03 interview](M03-interview-coaching.md), after M01/M02.
Delivery: [Combined M04–M07 implementation plan](../IMPLEMENTATION-PLAN.md#m04m07-execution-plan), with
shared neutral reports and PR access. This handoff retains M04-specific contracts.
Scope: [Review feedback](../DESIGN.md#review-feedback).
Criteria: [T11, T12, T13](../TESTING.md#criteria), plus affected host/preferences checks.

## Useful result

The user explicitly invokes a native Mentor review skill for local changes or a
PR. The primary agent reads the real change and relevant context, primes the
learner at the selected manual level, pauses for their review, then discusses
their observations alongside evidence-backed findings. It reports defects;
fixing code or publishing comments requires a separate request.

Ordinary defect reporting and required checks remain available without launching
this full skill. There is no automatic full review interview, proficiency score,
knowledge checkpoint or inferred level change.

## Review sequence

1. **Resolve the target.** Accept local changes or a PR. For local work, establish
   the relevant base and included staged/unstaged/untracked files; for a PR,
   obtain its diff, metadata and reviewed revision through the adapter. If no
   target is supplied, ask what to review rather than defaulting to uncommitted
   changes or the whole branch. Reuse an explicit target; clarify any ambiguity
   that changes the included scope. No PR is required for local use.
2. **Read the change and evidence.** Inspect the actual diff, relevant surrounding
   code, requirements and available check results. Record revision or local
   snapshot identity and inspected scope. Do not substitute a PR description for
   code or attribute earlier check results to a newer revision. Report inaccessible
   context and missing checks accurately. Run relevant focused existing checks
   when practical, using an isolated copy/checkout where needed to preserve the
   source checkout. Tie each result to the checked snapshot and covered behavior;
   unavailable checks remain pending with a concrete next check.
3. **Choose review concerns.** The primary agent identifies concerns relevant to
   the change, such as correctness, failure handling, readability, comments and
   documentation. No mandatory reviewer counts, subagents, exhaustive lens lists
   or unrelated hypothetical scale analysis.
4. **Prime the learner.** Before giving ordinary findings, explain what changed,
   intended behavior, relevant files/flow and useful things to inspect. Junior
   gets a code-flow walkthrough and correctness/test examples; Mid-level gets
   boundary/contract/failure prompts; Senior gets a concise primer about assumptions,
   tradeoffs and change risks. All profiles inspect readability, useful comments,
   documentation and correctness. Refer to the actual
   code. Prepare the learner to review without requiring a quiz or giving a grade.
5. **Pause for review.** With coaching on, wait for the learner's observations or
   request to see the findings. Do not infer that silence is a completed review.
   Direct-help or skip requests move straight to the report; no minimum attempt,
   answer quality or struggle quota is required. Coaching-off omits teaching and
   this practice pause, and delivers the review directly. Serious defects already
   identified are disclosed immediately rather than hidden for an exercise.
6. **Review and discuss.** Complete the evidence-backed review of the agreed
   scope. Relate the learner's observations to the actual code: explain what
   supports a finding, correct unsupported reasoning respectfully, and help form
   a useful review comment when relevant. Report every identified material defect
   even if teaching focuses on one flow. Keep required corrections/verification
   gaps, learning discussion and optional improvements visibly separate. Unknown
   behavior remains unknown until checked; a learning gap is not a product defect.
7. **Save and report.** Save a local review report under the neutral configured
   data root/project identity in a task-specific directory, without overwriting
   earlier reviews silently. Include target/revision, inspected scope, each
   finding's location/consequence/evidence, relevant check results, optional
   improvements and limitations. If the diff changes during the pause, refresh
   affected context and identify stale evidence before finalizing. Report storage
   failure honestly; do not claim an artifact was saved. Do not save a full learner
   transcript or proficiency ledger by default.
8. **Finish at findings.** Give the report location and relevant next checks.
   Do not edit code, create a PR, post comments or invoke a fixing workflow merely
   because review was requested. If the user separately asks for a fix, scope and
   verify it under the project's implementation agreements; findings alone do
   not establish that a correction exists or that checks pass.

## Evidence contract

- **Snapshot:** For a PR, record repository, base and head revisions. For local
  work, record the agreed base/HEAD, included staged/unstaged/untracked paths and
  a content digest or equivalent snapshot identity. HEAD alone does not identify
  dirty content. Identify the content actually inspected and checked.
- **Coverage:** Map relevant changed behavior/public contracts to actual check
  results and evidence references. Record command, result, checked snapshot and
  relevant configuration when known. A general build PASS does not prove an
  unexercised flow. Inspect supplied evidence rather than trusting its filename.
- **Appropriate checks:** Use the project's existing tests, CLI/API checks, native
  host receipts or UI/runtime/accessibility evidence as relevant to the change.
  Non-UI work has no screenshot requirement. No upstream evidence format or
  private service is required. Do not add a general evidence ingestion framework.
- **Freshness:** Newest does not mean relevant or current. Label stale, unrelated
  and unknown-provenance evidence accurately. Recheck affected content/results if
  the target changes during the learner pause; retain valid unrelated evidence.
  Update the primer when the changed scope makes the earlier primer misleading.
- **Findings:** Separate reproduced defects from required verification gaps. A
  defect has a location, trigger, consequence and supporting evidence. A gap has
  the uncovered behavior, why a check is required and the next concrete check.
  Missing proof does not establish defective behavior. Optional polish stays
  optional; an absent unrelated evidence pack is not a blocker.
- **Reports:** Save truthful scope/snapshot, evidence references, findings, check
  results, optional refinements and limitations. Preserve earlier reports. Save
  neither a full learner transcript nor proficiency/background tracking.

## Implementation plan

Implement the steps in order after a separate implementation request. The primary
agent handles the workflow; the plan assigns no learner coding quota. Use original
Mentor instructions and the recorded upstream attribution rather than copying
source with unconfirmed redistribution terms.

### 1. Canonical review workflow

Add `core/workflows/review.md` with the review sequence and evidence contract above.
Reuse the shared code policy and M02 manual level/coaching state. Keep target
clarification distinct from the learner practice pause: coaching-off and direct
findings bypass practice, but still resolve missing scope. Ordinary tasks retain
normal defect reporting without loading this full workflow. Reviews end at
findings; no automatic fix, posting or debugging/repair skill handoff.

Verify the workflow against the handoff before connecting the host wrapper.
Teaching/conversation behavior is verified through native turns, not exact prose
assertions.

### 2. Neutral report storage

Add shared `runtime/reports.py` for task-specific Markdown reports under
`<data-root>/projects/<project-id>/reviews/<local-date>-<task-slug>/review.md`.
Reuse validated explicit data-root/project identity handling. Reserve directories
exclusively with numeric collision suffixes. Restrict writes to this project's
reserved directories; never silently replace an earlier report or select another
root after failure. Publish complete reports safely and read them back before
claiming persistence. Surface failed/partial writes accurately.

Keep this separate from `InterviewArtifacts` confirmation/plan semantics. The
helper stores reports; it does not grade observations, change preferences, select
review concerns or certify an agent's findings.

Protect isolation, collisions, invalid paths/identity, existing-report preservation
and real storage failures through focused boundary checks.

### 3. Adapter-owned targets and snapshots

Add `adapters/codex/review_target.py` for local Git/PR resolution and snapshot
capture. Keep Git/PR transport and schemas out of the neutral workflow/runtime.
Use the agreed local scope: uncommitted changes, a branch/commit range or selected
files as requested. Record included staged, unstaged and untracked content,
renames/deletions and relevant file modes; excluded content stays outside the
reported scope. Preserve argument boundaries for paths and refs.

For PRs, obtain actual diff, metadata, base/head and surrounding code through
read-only host tooling. Use disposable checkouts/copies for execution when needed;
do not switch/reset the user's source checkout. A staged-only review must not
attribute results from different unstaged content to the index snapshot. Verify
the checked content and recapture target identity before finalizing. Missing
context, failed transport or an unavailable check produces an accurate limitation.

Protect selected-scope capture, equal HEADs with different dirty content, staged
versus worktree identity, PR revision resolution and visible failures with focused
entry-point checks. Do not add generalized hosting-provider support in this slice.

### 4. Native Codex skill and report entry point

Add a thin `adapters/codex/reports.py` entry point for the shared neutral report helper and
`adapters/codex/skills/mentor-review/` containing `SKILL.md`,
`agents/openai.yaml` and `scripts/context.py`. Follow the existing interview
wrapper's development-symlink/resource-resolution pattern. Disable implicit
invocation through native metadata. Return canonical resource paths and usable
adapter commands; receive the actual workspace, pinned data root and current M02
session object. Refresh defaults read-only without losing session overrides.

Update `adapters/codex/session_start.py` with concise explicit invocation guidance
and validation of advertised resources. Do not inject the full review workflow
into ordinary sessions. Keep hooks within their existing bounded context.

Verify actual skill registration/loading through the development host in an
external workspace. Cover another cwd/relocated checkout, resource failures,
unchanged preferences and an ordinary task that does not launch the review.

### 5. Check execution and report assembly

Connect target/snapshot inspection, existing check execution and report storage
through the primary agent workflow. Run focused checks at the relevant revision;
record failed checks, missing tools/context and uncovered behavior without claiming
PASS. Inspect supplied evidence for scope, result and provenance. Recheck affected
results after a target change during the pause and identify stale observations
before final discussion.

The final report contains target/base/head or local snapshot identity, inspected
files/flows, every identified material defect, required verification gaps,
commands/results/evidence references, optional refinements and limitations.
Relate discussion only to observations actually supplied. If persistence fails,
deliver findings with the failure notice rather than claiming a saved report.

### 6. Immediate verification

Add only meaningful boundary tests, following the development-time testAudit
authoring gate when tests are written. Run
`python3 -m unittest discover -s tests -v` after each affected executable portion.
Existing fixture checks own the expense calculation contract; do not duplicate
them or assert exact workflow wording.

Prepare S04's actual boundary-defect diff and optional polish in a disposable
fixture, with observer response cards outside the learner workspace. Exercise
local and PR native invocation, all levels, actual supplied observations,
direct-findings, coaching-off, different session/project preferences and a target
changed during the pause. A reproduced defect may correctly produce a failing
behavior check; review-only does not fix it or require a passing candidate.

Exercise missing/stale/unrelated evidence, report collisions/storage failures,
missing resources/context and ordinary-task behavior. Check native behavior with
the current installed hooks, including deliberate waits; preserve existing hook
configuration and record conflicts instead of patching private toolkit files.
Rerun affected disabled/untrusted hook controls if delivery changes. Compare
source/preference state before and after review-only runs.

Use the [M04 verification matrix](../TESTING.md#m04-verification-matrix). Record
actual native delivery, scripted conduct, software correctness/readability and
observed human learning separately. Policy or wrapper files alone establish no
native pass or learning outcome.

### 7. Documentation and evidence handback

Update `runtime/README.md` and `adapters/codex/README.md` with report layout,
explicit invocation, target clarification, check execution and failure behavior.
Add `docs/evidence/M04.md` after running the scenarios, with revision/snapshot,
host/model/language, evidence references, actual results and pending checks.
Inspect resulting implementation/comments/docs for readability.

Update this handoff, `README.md`, `docs/ROADMAP.md`, `docs/TESTING.md` and
`docs/IMPLEMENTATION-PLAN.md` only to the status supported by those results.
Retain historical M01–M03 evidence and append accurate source attribution.

Public packaging/discovery/installation/publication remain M08. Automatic fixes,
comment posting, proficiency assessment, adaptive levels, specialized reviewer
orchestration and a full evaluation runner are outside M04.

## Immediate acceptance

- [ ] Native explicit invocation works for both a local diff and a PR in an external
  workspace without private integrations. A normal task does not launch the full
  review skill; ordinary material-defect reporting remains available.
- [ ] An unspecified target prompts for what to review. An explicit target is reused,
  with ambiguous scope clarified. The agreed base/PR revisions and included dirty
  content identify the actual inspected and checked snapshot.
- [ ] S04's actual diff/context is inspected. The known boundary defect is reported
  with location, consequence and independent reproduction/check evidence. Optional
  polish is separate; all identified material defects appear in the final report.
- [ ] Junior, Mid-level and Senior provide their task-relevant primer before findings;
  all retain correctness and readable-code/comment/documentation expectations.
  Coaching-on then pauses for observations; no attempt is fabricated and no score
  or inferred level change occurs. Effective/saved preferences remain unchanged.
- [ ] After a learner response, evidence supports or corrects their observations and
  helps explain a useful review comment. Serious defects are disclosed immediately.
  A direct-findings request skips the wait; coaching-off provides a direct report.
- [ ] The report preserves target/revision, inspected scope, evidence, checks and
  limitations. A changed diff refreshes affected context; missing context, failed
  storage and report-directory collisions are handled accurately.
- [ ] Relevant focused existing checks run when practical. Evidence maps to changed
  behavior and the checked snapshot. Newest-but-unrelated, stale and unknown results
  do not establish a current PASS. Required verification gaps are separate from
  reproduced defects, with a concrete next check; non-UI work requires no screenshot.
- [ ] Review-only runs leave code untouched and do not post comments or start fixing.
  Any separately requested correction receives its own real checks and readable
  code/comments/docs. The review runs its relevant checks; a passing corrected
  implementation is not required merely to report a defect.
- [ ] Record actual invocation, conduct and check evidence separately from observed
  human learning. Usage and attribution are accurate; unperformed checks stay pending.

M01–M04 become the first local usable version only after their required criteria
have passing evidence. Planning alone does not establish delivery or human learning.

## Handback

Report the target and inspected revision/scope, material findings with evidence,
optional refinements, actual checks/limitations and saved report location. Connect
learning discussion to supplied observations without an assessment of ability.
