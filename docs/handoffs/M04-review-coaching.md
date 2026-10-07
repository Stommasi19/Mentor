# M04 — explicitly invoked review skill with learner priming

Status: Revised plan confirmed on 2026-10-06; implementation and verification
have not started.
Dependency: [Revised M03 interview](M03-interview-coaching.md), after M01/M02.
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
   obtain its diff, metadata and reviewed revision through the adapter. Ask only
   when target ambiguity would change the review. No PR is required for local use.
2. **Read the change and evidence.** Inspect the actual diff, relevant surrounding
   code, requirements and available check results. Record revision or local
   snapshot identity and inspected scope. Do not substitute a PR description for
   code or attribute earlier check results to a newer revision. Report inaccessible
   context and missing checks accurately.
3. **Choose review concerns.** The primary agent identifies concerns relevant to
   the change, such as correctness, failure handling, readability, comments and
   documentation. No mandatory reviewer counts, subagents, exhaustive lens lists
   or unrelated hypothetical scale analysis.
4. **Prime the learner.** Before giving ordinary findings, explain what changed,
   intended behavior, relevant files/flow and useful things to inspect. Guided
   gets a walkthrough with concrete examples; supported gets a flow map and
   focused prompts; independent gets a brief scope/checklist. Refer to the actual
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

## Future implementation

1. Inspect upstream `review` version and terms; record attribution and required
   notices for permitted copies, or author original instructions from this plan.
   Adapt its target/context/evidence/review/report sequence without private paths,
   named private reviewers, memory services or orchestration dependencies.
2. Add one neutral `core/workflows/review.md` and a thin native host skill wrapper
   registered through supported local development facilities. Verify explicit-only
   invocation in the actual host. Keep host PR APIs/schemas and skill metadata in
   the adapter; do not assume an unverified slash-command spelling.
3. Use M02's effective manual level and coaching state, preserving session/saved
   distinctions. Skill invocation writes no preferences or automatic learner state.
   Keep always-loaded guidance concise; ordinary defect reporting remains active.
4. Implement only necessary neutral report handling. Exercise primer/pause/report
   with the actual host in an external workspace and record usage and limitations.

Public packaging/discovery/installation/publication remain M08. Automatic fixes,
comment posting, proficiency assessment, adaptive levels, specialized reviewer
orchestration and a full evaluation runner are outside M04.

## Immediate acceptance

- [ ] Native explicit invocation works for both a local diff and a PR in an external
  workspace without private integrations. A normal task does not launch the full
  review skill; ordinary material-defect reporting remains available.
- [ ] S04's actual diff/context is inspected. The known boundary defect is reported
  with location, consequence and independent reproduction/check evidence. Optional
  polish is separate; all identified material defects appear in the final report.
- [ ] Guided, supported and independent provide the agreed primer before findings.
  Coaching-on then pauses for observations; no attempt is fabricated and no score
  or inferred level change occurs. Effective/saved preferences remain unchanged.
- [ ] After a learner response, evidence supports or corrects their observations and
  helps explain a useful review comment. Serious defects are disclosed immediately.
  A direct-findings request skips the wait; coaching-off provides a direct report.
- [ ] The report preserves target/revision, inspected scope, evidence, checks and
  limitations. A changed diff refreshes affected context; missing context, failed
  storage and report-directory collisions are handled accurately.
- [ ] Review-only runs leave code untouched and do not post comments or start fixing.
  Any separately requested correction receives its own real checks and readable
  code/comments/docs; no such checks are required merely to report a defect.
- [ ] Record actual invocation, conduct and check evidence separately from observed
  human learning. Usage and attribution are accurate; unperformed checks stay pending.

M01–M04 become the first local usable version only after their required criteria
have passing evidence. Planning alone does not establish delivery or human learning.

## Handback

Report the target and inspected revision/scope, material findings with evidence,
optional refinements, actual checks/limitations and saved report location. Connect
learning discussion to supplied observations without an assessment of ability.
