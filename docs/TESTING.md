# Mentor verification plan

Status: M01's core, development adapter, fixture, executable checks, and local runs
are implemented. [M01 results](evidence/M01.md) cover T01–T05, T12, and T13
architecture. [M02 results](evidence/M02.md) on 2026-10-06 cover the required manual
control/preference contracts, native lifecycle/refresh, conduct simulations and
generated-code checks for the recorded combination. [M03 results](evidence/M03.md)
cover the original workflow's requirements, invocation, mistake/direct-help and
paused conduct with independent generated-code checks.
[Revised M03 results](evidence/M03-revised.md) cover native explicit invocation,
stages/confirmation/artifacts, manual levels, scope/failure cases, and C# checks.
The [combined M04–M07 implementation plan](IMPLEMENTATION-PLAN.md#m04m07-execution-plan)
includes both ordinary core uses, review/feedback/PR self-check skills, optional
Serena and creation/existing-code trials. [Current evidence](evidence/M04-M07.md)
records 26 passing boundary tests, generated fixture results and source trials.
Selected native conduct/navigation and disposable pinned-SDK build/HTTP checks pass;
remaining observations are identified in the evidence, not assigned blanket passes.
Junior/Mid-level/Senior profiles and legacy-state compatibility are part of that
delivery. Historical M02/M03 results cover Guided/Supported/Independent, not these
new profiles. Readable code, useful comments and documentation remain required
at every level and with coaching paused.
Automatic mid-turn compaction, broader compatibility and human learning remain pending.
Scope and ownership: [IMPLEMENTATION-PLAN.md](IMPLEMENTATION-PLAN.md).

## Evidence and results

Use `pass`, `fail`, or `pending` per criterion. A pending host interaction is
not a pass; record the unavailable action or missing observation. For mentoring
judgments, use `inconclusive` when the transcript cannot support a conclusion.
Do not hide an actual defect inside an aggregate score.

| Evidence | Establishes |
| --- | --- |
| Policy-only experiment | The supplied core influenced behavior in this explicitly configured run; no automatic-delivery claim. |
| Development hook execution and delivered context | The real host automatically loaded this core revision. |
| Behavioral code checks | The resulting code satisfies the checked requirements. |
| Readability review of code/comments/docs | This change is understandable, maintainable, and its non-obvious intent/contracts are documented appropriately. |
| Transcript observations with turn references | Mentor followed the relevant interaction criteria in this run. |
| Unaided human explanation, prediction, or diagnosis | Observed comprehension on that task; a small pilot does not establish a causal learning improvement. |

For a slice, record core/adapter/host/model/provider versions, language, settings, fixture/scenario
version, starting preferences, actual hook evidence, transcript turns, authored
contributions, final diff, commands/results, criterion judgments, and limitations.
Record failed runs too. Keep raw local transcripts outside public Git; publish
sanitized examples only through a separately requested release/demo task.

## Reusable fixture

Start with a tiny C# expense-summary project: records containing a date, category,
and decimal amount, plus a function that totals matching expenses. No database,
web server, real user data, or DoughTracker dependency is needed.

M01 supplies this fixture under `fixtures/expense-summary/`; run disposable copies
outside Mentor. Version the starter, public task, scripted learner response cards,
and independent checks.
C# is an initial test case, not a core requirement. Record the actual .NET SDK/
target and model/provider. Restore the starter and a controlled preference
record before each run. Reuse the domain while changing the task and misconception.
Spending is a sample coding task; it is not a feature of Mentor. M03 supplies
S02's task and observer response cards alongside the existing S01/S03 scenarios.

| Scenario | Task | What to observe |
| --- | --- | --- |
| S01 — small implementation | Total a category; clarify matching semantics and document the chosen public contract. | Correct/readable code, useful comments/docs in the code, decision/prediction, conditional coding offer, takeover respected. |
| S02 — requirements | “Show spending for this month and category,” with month boundaries and refund behavior open. | Learner reasoning informs focused clarification; chosen rules and unresolved assumptions are recorded. |
| S03 — incorrect attempt | Learner includes an expense at the next month's boundary in the current month. | Mentor responds to the actual error with a useful investigation/hint, then verifies the agreed interval. |
| S04 — review | A diff includes that boundary defect plus a harmless naming/style refinement. | Level-specific primer, pause for learner review, then evidence-backed discussion and complete findings; optional polish distinct; no automatic fixes/posting. |

The public specification fixes agreed rules before code checks run: inclusive
start and exclusive end for the selected month, decimal arithmetic, and the
user's explicit decisions about matching/refunds. Private checks must test those
requirements rather than impose unasked business rules or exact implementations.

Reserve a related scenario from prompt tuning, such as an empty-category or
year-boundary variation selected during implementation. Repeat known cases to
catch regressions; use the reserved case after stabilizing the policy. Refresh
reserved cases if their details become tuning input. One memorized conversation
does not demonstrate generalization.

M01 exercised the fixture's current reserved examples. If M02 changes are tuned
against those examples, select and record a fresh reserved variation before the
final conduct/code-quality check; do not label the existing examples unseen.

## Language, model, and host coverage

The core policy/workflows and rubric use generic concepts and follow the target
project's idioms. C#/.NET details stay in its fixture; provider/host input schemas
stay in adapters. Using Python for helper scripts does not mandate Python code
from learners.

M01 records initial C#/model/host results. M05 repeats equivalent scenarios in a
second coding language and with models from at least two providers where access
exists. Apply the same quality/conduct criteria with language-appropriate checks.
For the combined delivery, use a standalone Python fixture alongside C# and
existing OpenAI access. Other providers remain unverified/pending; require no
new paid model accounts. Stafr's TypeScript source trial records its own inspected
scope and check results without implying equivalent full fixture coverage.
Record each actual language/model/provider/host combination, policy revision,
result, and pending limitations. Lack of access is pending, not compatibility
proof. Representative coverage does not establish support for every combination.

A second host's actual automatic loading requires its own adapter/trace. Directly
supplying policy to another LLM tests core behavior without proving hooks on that
host. Marketplace/install tests belong to final M08, not this portability check.

## Actors and comparison

Start with a person or scripted responses. Reactive simulated juniors can follow
once the basic interactions work; a full runner is a later milestone.

A junior receives only public task/code, a concrete prior-knowledge/misconception
profile, and the conversation. An observer receives evidence and criteria. Keep
the mentor policy, private checks, reference answers, and rubric away from the
junior. Fresh context does not isolate files: use an actor without file tools or
enforced access restrictions. Label ordinary shared-filesystem role-play a
development simulation when isolation cannot be demonstrated.

Scripted cards include an initial partial idea, a mistake, a request for a hint,
and a takeover request; choose the relevant reply based on what Mentor actually
asks. Do not force a response to a question it never asked. Fresh agents should
not inherit earlier answers or test transcripts.

Use bounded runs, initially up to eight learner/mentor exchanges per scenario;
record completion, timeout, takeover, code failure, or inconclusive behavior.
This is an evaluation budget, not a product quota. Repeat a changed policy on
the affected scenario when a failure or new behavior warrants it.

M01 includes one controlled baseline/core comparison to inspect the produced
code/comments/docs before adding distribution work. Hold model/settings, starter,
task, response profile, and unrelated configuration constant for each comparison.
Reset preferences/context.
Exclude Mentor policy from baseline hooks and project instructions, including
this repository's AGENTS.md. Baseline comparison informs evaluation; it is not
required for every unrelated implementation edit. If the baseline already meets
the criteria, record that; do not manufacture an improvement claim. Review
samples and disputed observer judgments manually.

## Criteria

| ID | Slice | Observable criterion | Immediate method |
| --- | --- | --- | --- |
| T01 | M01 | A real local development hook delivers this core automatically to a fresh host session without pasting policy or invoking a skill. Disabled/untrusted hook supplies no such context. | External disposable workspace and supported development hook config; capture core/adapter revision and actual host execution/context evidence. Marketplace not required. |
| T02 | M01 | Development adapter emits the host's valid event output with nonempty shared policy when invoked from another directory; absent core policy fails visibly. | Execute the real adapter entry point with synthetic event input and missing-resource case. This tests the adapter contract, not actual host delivery. |
| T03 | M01, M02 | Lifecycle reloads policy; M02 also loads project defaults and requires startup/resume/manual compaction/clear with saved settings. Resume/compaction retain session overrides, while clear starts from saved values. | Record each native lifecycle separately. Automatic mid-turn compaction remains separately pending; handler event coverage alone does not prove delivery. |
| T04 | M01 onward | Generated code is behaviorally correct, readable, maintainable, and appropriately commented/documented in the project language. Comments explain intent/non-obvious rules; public contracts are accurate. | Run S01 independent checks and annotate actual code/comments/docs. Compare baseline/core outputs; record concrete strengths/defects, not just teaching prose or formatter success. |
| T05 | M01, M02 | A learner coding offer is meaningful and conditional; demonstration/takeover or agent-implements project agreements receive complete work. | S01 with a decision/attempt and takeover variant; check authored contribution and actual completed code. |
| T06 | M02 baseline; M04–M07 profiles | Junior focuses on code understanding/safe changes, Mid-level on feature ownership/design, Senior on engineering judgment/tradeoffs. All retain readable code, useful comments/docs and requested direct help; ownership is separately overridable. Historical M02 conduct uses legacy names. | Repeat the same task under all three profiles with fresh context. Observe different task-relevant concerns, not just verbosity. Inspect resulting code/comments/docs; verify ownership/topic-help overrides do not change levels. |
| T07 | M02 | Session controls make no storage changes; explicit project changes persist. Projects remain separate, repo subdirectories/worktrees share settings, and updates preserve the other saved field. Status refresh retains local overrides and shows effective/saved values. | Real temporary roots/worktrees, hook/control round trips, fresh native sessions, and two already-open sessions with/without overrides. Include non-Git roots, symlinks, explicit data locations, and differing hook/tool cwd. |
| T08 | M02 | Pause removes compulsory teaching while retaining code standards. Missing state defaults; invalid state warns and stays intact until explicit reset. Failed writes/resets apply requested values locally with an unsaved warning. Project reset clears current overrides; other sessions retain their own. | Coaching-off S01 and control round trips with invalid/unsupported/unreadable state and unavailable/read-only storage. Confirm prior-record preservation, effective/saved values, and reset isolation. |
| T09 | M02 | Mentor responds to the learner's mistake and offers increasingly useful help; a direct help request is honored. | S03 transcript and final behavioral check; no struggle quota or invented proficiency judgment. |
| T10 | Revised M03 | Native explicitly invoked interview follows setup, focused rounds, teaching preferences, summary/confirmation, artifacts and scoped execution/handoff. No subagents or automatic full interview; manual levels shape explanations. | Actual host invocation; S02, all three levels, ordinary-task negative control, settled/skip/paused cases, requirements-only and confirmed execution/handoff. |
| T11 | Revised M04 | Explicit native local/PR review reads the actual change, primes at the manual level, pauses for learner review, then discusses observations and reports material findings with evidence. Optional polish separate; report-only. | Actual host invocation for both targets, S04 reproduction/check, all primers, pause/skip/coaching-off, saved report/revision accuracy and unchanged preferences. |
| T12 | All | Policy experiment, actual hook delivery, code quality/conduct/comprehension claims have the correct evidence; unperformed checks remain pending. | Inspect handback and cited artifacts. Neither policy-only runs nor synthetic actors prove automatic delivery or human learning. |
| T13 | M01 architecture; M05 coverage | Core has no target-language/vendor/host assumptions; compatibility claims reflect actual tests. | Inspect core/adapter boundary, then exercise representative languages and providers with the same rubric. Record a support matrix and pending cells. |
| T14 | M08 only | Verified core is packaged for others; discovery/install, trust, updates/removal, and release docs match supported behavior. | Final clean-environment distribution checks after local product/portability evidence. No early marketplace gate. |
| T15 | Revised M06 | Explicit feedback uses available current-task evidence immediately and saves a local Markdown report. Reflection optional, levels manually selected, no background tracking or automatic fixes. | Actual native invocation, all three levels/coaching-off, ordinary-task negative control, work-in-progress/missing-observation cases, report evidence/storage checks and unchanged preferences. |
| T16 | M05 optional tooling | Opt-in Serena semantic navigation works through the actual host, falls back when unavailable, and preserves mentoring/ownership/preferences. Efficiency or quality claims require controlled evidence. | External workspace activation and symbol/reference calls, no-server/failure cases and a bounded same-task comparison; inspect code/comments/docs and available metrics. |
| T17 | M06 PR self-check | Explicit GitHub PR skill reads actual diff/context/tests, asks grounded questions, waits for supplied answers or help requests, and explains with evidence. Preferences unchanged; local Markdown and no code/PR mutations. | Native invocation/retrieval, correct/mistaken/assisted/unattempted answers, hint/skip/stop, changing PR, report failures and honest evidence claims. |
| T18 | Core/M07 existing-project understanding | Ordinary help explains actual existing source/flow and verification limits without requiring a diff, PR, full skill, quiz or report. | Stafr/Crew Workforce source-grounded walkthrough at manual support levels, concrete locations, actual failure/check evidence where available and accurately labeled uninspected scope. Human understanding is observed separately. |

T04 review questions:

- Can another developer trace the changed behavior and explain the names?
- Do boundaries and abstractions serve the current behavior?
- Do comments in the code explain intent, assumptions, and non-obvious rules?
- Are public contracts and verification docs accurate and useful to another developer?
- Does the code handle the agreed failure/boundary case, and do checks demonstrate it?

A readability review records a concrete example and any necessary correction.
Do not invent universal method-length limits, comment quotas, or subjective scores
as release gates. Disclose every identified material defect even when the
conversation concentrates on one learning topic.

## M02 verification matrix

Use the [preference operation table](IMPLEMENTATION-PLAN.md#preference-precedence-and-lifetime)
and [M02 handoff](handoffs/M02-manual-levels-and-preferences.md) as the expected
contract. Every required row has a recorded local pass in [M02 evidence](evidence/M02.md).
Keep executable checks, native delivery, conduct, and
code-quality results separate; this matrix is not a new evaluation runner.

| Boundary / criterion | Required observation | Evidence |
| --- | --- | --- |
| Control scope and defaults — T07/T08 | Missing record gives guided/on; status and unqualified level/pause/resume create no storage or change an existing record. Explicit project changes save only the requested field, preserving the other saved field even when its session value differs. Invalid actions do not mutate state. | Actual helper/wrapper entry points, real files and readback; current-conversation responses distinguish session/project scope. |
| Identity and data location — T02/T07 | Repo subdirectories/worktrees and canonical/symlink paths share settings; separate clones/projects do not. Non-Git roots follow documented limits. Hook/control calls agree from different cwd and receive the resolved data root explicitly. Lookup/configuration failures warn rather than select another record. | Real temporary repos/worktrees/non-Git roots and actual adapter/control entry points. |
| Recovery and atomic writes — T08 | Missing, malformed, unsupported, unreadable, and unavailable/read-only storage follow the contract. Ordinary mutations preserve invalid records; failed writes preserve the prior record and apply locally as unsaved. Explicit reset restores only this project's defaults/current overrides, or reports unsaved local defaults. | Helper/hook/control results, filesystem before/after, and conversation evidence; include actual permission failures. No cross-session merge claim. |
| Extended hook and control delivery — T01/T02 | The native host delivers valid policy, project defaults/warnings, and usable control guidance. An actual control resolves the same project/root without assuming hook environment variables in ordinary tools. Preference failures retain policy; core-resource failures stay visible. | Native execution/context and control result in an external workspace. Synthetic handler checks cover contracts only; rerun affected disabled/untrusted controls. |
| Saved-state lifecycle — T03 | Startup loads saved settings; resume/manual compaction reload defaults while retaining a different session override; native clear starts from saved settings without that override. | Separate native runtime traces and effective/saved observations for all four events. Automatic mid-turn compaction is separately pending, not required for M02 completion. |
| Two open sessions — T07/T08 | A project change in A is adopted in B after status when B has no local override. With B's own override, status reloads/shows the saved change but retains B's effective choice. A session-only change in A does not affect B or disk. Reset in A retains B's override after refresh. | Two actual host conversations sharing a project, controlled state, control results, and turn references; no live-broadcast assumption. |
| Levels and coaching off — T04/T05/T06/T08 | Repeat S01 from the same starter under guided, supported, independent, and coaching-off. Conduct changes appropriately; code/comments/docs and behavior still meet requirements. Takeover/project ownership agreements get complete verified work. | Fresh contexts/controlled preferences, transcripts, final diff, independent checks, and annotated readability review. Reuse M01's baseline evidence unless a new comparison is warranted. |
| Mistake and direct help — T05/T09 | Prepare S03's incorrect month-boundary attempt; give a useful hint/escalation and honor direct-help/takeover without changing saved level. Verify the corrected implementation. | Focused S03 transcript and final behavioral checks, with authorship/assistance recorded. No proficiency or human-learning claim from a scripted actor. |

Record session overrides as well as starting saved preferences for each run.
Keep raw host/conversation evidence outside public Git and add an M02 evidence
report after implementation. The M01 report stays historical evidence for its
tested revision; its passes do not verify the extended M02 adapter or controls.

## M03 verification matrix

Use the [revised M03 handoff](handoffs/M03-interview-coaching.md) as the contract.
[Revised M03 results](evidence/M03-revised.md) record the local results below.
[Original M03 results](evidence/M03.md) verify the earlier workflow only. Use actual native skill invocation in an external
workspace; keep observer inputs and independent checks outside the learner workspace.

| Boundary / criterion | Required observation |
| --- | --- |
| Native invocation — T10/T12/T13 | Registered host skill explicitly invoked, with actual runtime evidence of the canonical workflow loading. Ordinary tasks do not launch the full interview; essential clarification still works. Local setup survives relocation/another cwd without private services. Record affected resource failures. |
| Staged process — T10 | S02 retains target/request/time box, high-level questions, primary-agent teaching preferences, drill-down and concrete summary. Reuse supplied answers. No subagent offers, spawning or orchestration. |
| Teaching and preferences — T06/T10 | Same essential task under guided, supported and independent demonstrates examples/framing, approach/tradeoff support and concise decisions respectively. Effective/saved choices remain unchanged even when different. No exercises, grading or inferred level changes. |
| Pacing and pause — T08/T10 | Substantial interviews use the upstream-like stages; settled tasks and skip requests avoid invented questions. Paused coaching retains clarification, confirmation and artifacts without teaching prompts or changing preferences. |
| Confirmation and scope — T10 | No execution before concrete-plan approval. Requirements-only leaves code untouched. Confirmed already-authorized work continues without a second blanket gate and receives its relevant checks. A planning task does not authorize implementation. |
| Artifacts and handoff — T10/T12 | Interview and plan contain the confirmed request, target, constraints, answers, approach, assumptions and checks. An available target receives original request, constraints and artifact references. Check unavailable target, persistence failure and task-directory collision handling. |
| Resulting code and evidence — T04/T12 | Inspect actual code/comments/docs and independent checks when execution produces code. Record native invocation, simulated conduct, software correctness and observed human learning separately; no historical pass is attributed to this revision. |

Do not turn workflow prose into exact-wording tests. Meaningful process-boundary
checks cover registration/resource/artifact failures; recorded conversations assess
stages and teaching. Existing fixture checks own the agreed calculation contract.
M02 retains its mistake/direct-help checks under T09; M03 does not acquire a
separate learner knowledge checkpoint. Broader portability and invoked task feedback follow later.

## M04 verification matrix

Use the [M04 implementation plan confirmed on 2026-10-07](handoffs/M04-review-coaching.md#implementation-plan),
including its adopted evidence contract. Implementation and selected native
observations are recorded in [current evidence](evidence/M04-M07.md); the matrix
below remains the required coverage, not a claim that every row has passed.

| Boundary / criterion | Required observation |
| --- | --- |
| Native invocation and target — T11/T12/T13 | Actual host skill invocation works for local changes and a PR without private paths/services. With no target, ask what to review rather than assuming a scope. Reuse explicit targets and resolve ambiguity. Record repository/base/head or local base/revision and agreed staged/unstaged/untracked scope. Ordinary tasks do not launch the full skill; normal defect reporting remains available. |
| Primer and pause — T06/T11 | Junior code-flow/correctness/test examples, Mid-level boundary/contract/failure prompts and Senior assumptions/tradeoffs/change-risk primers precede ordinary findings. All inspect readability/comments/docs and correctness. Coaching-on waits for supplied observations or a direct-findings request; silence does not count as a review. |
| Evidence and discussion — T11/T12 | S04's diff/context is read; its defect has a location, consequence and independent reproduction/check. Discuss supplied observations with supporting/correcting evidence; report every identified material defect, optional polish separate and serious findings immediately. No grade or level inference. |
| Skip, coaching and preferences — T08/T11 | Direct-findings requests skip the wait; coaching-off gives a direct report. Effective/saved preferences remain unchanged, including different session overrides and project defaults. |
| Report and revision — T11/T12 | Local report records target/revision, inspected scope, findings/evidence, checks and limitations. Changes during the pause refresh affected context. Missing context, persistence failure and directory collisions are reported accurately; no full learner transcript or proficiency ledger is saved by default. |
| Focused checks and coverage — T11/T12 | Run relevant existing checks when practical in an appropriate isolated copy/checkout, preserving the source checkout. Record command, result, snapshot and covered behavior. Inspect supplied results; a general build PASS does not prove an unexercised flow. Non-UI changes acquire no screenshot or upstream evidence-format requirement. |
| Evidence relevance and freshness — T11/T12 | Matching scope/snapshot supports the claimed check result. Newest-but-unrelated evidence is not reused as proof. Stale and unknown-provenance results remain labeled accurately. A change during the learner pause refreshes affected context/checks and, when necessary, the primer; valid unrelated evidence remains usable. |
| Dirty/staged snapshot identity — T11/T12/T13 | Equal HEADs with different included dirty content have distinct snapshot identities. Capture the agreed staged/unstaged/untracked scope, including relevant modes and renames/deletions. Staged-only checks use the index content rather than attributing a different worktree result to it. PR checks identify the actual base/head and checked revision. |
| Defects versus verification gaps — T11/T12 | A reproduced defect records location, trigger, consequence and evidence. A missing required check records uncovered behavior, why it matters and a concrete next check; missing proof does not become an invented code defect. Optional polish and unrelated missing evidence packs are not blockers. |
| Report persistence boundaries — T11/T12 | Separate review directories preserve earlier reports. Invalid identity/root, wrong-project paths, collisions and actual failed/partial writes remain visible. No silent overwrite, fallback root, preference write or successful save claim without readback. |
| Report-only scope — T11/T12 | No automatic code fixes, PR creation, comment posting or fixing-skill invocation. Any separately requested correction has its own scope and real checks; findings alone do not establish corrected software or passing tests. |
| Combined native hooks — T01/T02/T06/T11/T12 | Actual development-host receipts show invocation under the current installed hooks; ordinary tasks stay ordinary and intentional learner waits remain waits. Preserve hook configuration and report observed conflicts. Rerun affected disabled/untrusted delivery controls when hook behavior changes. |

Review behavior is assessed through concrete transcript turns and code/check
evidence, not exact prose, finding quotas or inferred comprehension. Artifact and
host entry checks should protect meaningful boundaries. Keep actual host delivery,
simulation, software correctness and human learning as separate claims.

## M05 verification matrix

Use the [M05 contract](handoffs/M05-portability-and-tooling.md) within the combined
delivery. [Current evidence](evidence/M04-M07.md) records actual navigation,
portability and fallback checks, actual read-only model calls and a bounded
same-task build comparison. Its time/token observations establish no efficiency benefit.

| Boundary / criterion | Required observation |
| --- | --- |
| Repository setup and reuse — T16 | Repository-owned helpers/examples/README support opt-in setup without private toolkit paths. Reuse a compatible existing host connection; no duplicate registration or silent overwrite. Configuration presence does not prove live tools. |
| Actual host navigation — T12/T16 | Observe project activation and supported symbol/reference/structure calls in an external workspace, including another cwd/worktree. Record actual host/Serena/backend versions and language prerequisites. |
| Optionality and contract retention — T05–T08/T16 | Absent/disabled/failing Serena produces visible ordinary-tool fallback. Levels, coaching and ownership remain unchanged; no full-skill activation, memory/onboarding or background learner tracking. |
| Code and efficiency evidence — T04/T12/T16 | Bounded same-task/model/preferences/starter comparison with/without Serena records actual code/comments/docs, available tokens/calls/time and startup overhead. Missing metrics and unchanged/worse outcomes stay accurate. |
| Language/provider coverage — T12/T13 | Independent C# and Python cases identify actual OpenAI model/host/check results. Other providers stay pending without paid-account prerequisites or universal compatibility claims. Any TypeScript real-project check is reported at its actual scope. |

## M06 verification matrix

Use the [M06 handoff](handoffs/M06-task-feedback.md) for feedback and the separate
PR self-check. [Current evidence](evidence/M04-M07.md) records immediate feedback,
question/hint/explanation/pause/stop/report behavior, correct/mistaken/valid-alternative
scripted answers, and changed-revision conduct through labeled recorded transport.
Planning checks are not runtime evidence; naturally changing live-PR and human
understanding observations remain unperformed.

| Boundary / criterion | Required observation |
| --- | --- |
| Invocation and scope — T15/T12/T13 | Actual registered host skill is explicitly invoked and reuses the task at hand. Ordinary work creates no feedback report or learner ledger. No private paths/services or automatic full interview/review activation. |
| Immediate evidence-backed feedback — T15/T12 | Concrete strengths, improvements and optional next step cite the inspected task evidence. No reflection prerequisite or quiz; missing observations/checks and work in progress stay unknown/pending. Material defects and verification gaps are separate from optional refinements. |
| Manual levels and coaching — T06/T08/T15 | Junior code behavior/safe changes, Mid-level connected design/contracts/verification and Senior assumptions/alternatives/consequences follow controlled manual profiles. Coaching-off gives direct feedback. Readable-code/comment/doc standards remain active. Effective/saved preferences remain unchanged, including differing session overrides; explicit level changes retain M02 scope semantics. |
| Local Markdown — T15/T12 | Report contains task/scope, evidence, feedback, checks and limitations outside public Git. Check directory collisions and failed saves. No full transcript, proficiency profile, ongoing ledger or fabricated saved artifact. |
| Authorship and scope limits — T15/T12 | Agent-written work or passed checks alone causes no human-learning claim; supplied reasoning is identified accurately. No automatic progression/grades, fixes, posting or compulsory practice. Optional reflection remains available. |
| PR target and questions — T12/T13/T17 | Actual native invocation resolves a supplied GitHub PR and reads diff/context/tests at recorded base/head. Questions and answer guidance have specific code/test evidence. Invalid/inaccessible targets do not generate invented content. |
| Attempts and help — T17 | All three manual styles support correct/mistaken/valid alternative reasoning. Explanations wait for supplied answers or help requests; hint, direct explanation, skip and stop work. Assisted/unattempted answers are distinct from independent reasoning. Serious defects are disclosed immediately. |
| Self-check preferences and scope — T17 | Explicit self-check works with coaching paused without resuming it or changing overrides/defaults. Ordinary tasks/feedback/review do not launch a quiz. No code edits, posting, approval/merge, fixing workflow, proficiency grading or ledger. |
| Self-check reports/freshness — T12/T17 | Local Markdown records actual questions/answers/assistance, revision/scope and limitations. Changed PRs refresh affected context or identify the recorded-revision limit. Collisions/storage failures stay visible; scripted responses do not establish human understanding. |

Use existing task scenarios and reports where suitable; do not create an evaluation
runner or proficiency threshold to satisfy this slice. Process checks protect real
invocation/storage boundaries; transcript/report evidence assesses useful feedback.

## M04–M07 combined verification

Use the [combined implementation plan](IMPLEMENTATION-PLAN.md#m04m07-execution-plan).
Use [current evidence](evidence/M04-M07.md) to distinguish observed checks from
pending coverage; verify within one delivery, retaining component-specific evidence. Unavailable cross-provider or later human observations
do not become fabricated passes or block otherwise verified local use.

| Use/boundary | Required observation |
| --- | --- |
| Ordinary creation help — T04–T06/T12 | Fresh coding work uses the manually selected support and explicit ownership request. An accepted contribution has context and useful help; direct explanation/takeover receives complete verified work. Generated code/comments/docs meet T04 without a fixed contribution/comment quota. |
| Profile focus and shared foundation — T04/T06/T08 | Run the same backend behavior under Junior, Mid-level, Senior and paused coaching. Junior traces code and safe changes; Mid-level examines connected design/contracts/failures/tests; Senior examines assumptions, alternatives and consequences proportional to the task. Inspect actual generated names/flow, useful intent/rule comments and accurate docs in every condition. Topic-specific help/ownership requests are honored without changing preferences or inventing scale requirements. |
| Legacy-state compatibility — T03/T07/T08 | Valid version-1 saved levels and retained session overrides translate read-only to canonical profiles; status identifies translation and effective/saved state. Legacy controls act as aliases. Only explicit project writes/reset save version 2, preserving the other field. Exercise invalid versions/enums/types, atomic/readback/write failures, two-session refresh and native startup/resume/manual compaction/clear/interview with new values. Historical results do not establish these checks passed. |
| Existing-project help — T06/T12/T18 | Stafr/Crew Workforce explanation reads actual source/tests, maps relevant responsibilities and traces one real flow with locations, boundaries, failures and check limits. No diff/PR/full-skill/quiz/report prerequisite; unexplored scope remains explicit. |
| Shared host/report infrastructure — T01/T02/T07/T08/T11/T15/T17 | Real native delivery, effective/saved preferences, project isolation, target/snapshot freshness and failure-aware report storage work across the three distinct workflows. Ordinary help does not implicitly activate them or write reports/preferences. |
| Optional Prism / existing-server reuse — T01/T02/T07/T12/T15 | Use an already exposed connection, inspect aliases/plugins without registering a duplicate or choosing another port, load the explicitly selected project, save requested project-only facts and read them back. Test foreign-workspace bindings, supplied versions/conflicts, unknown learner fields, malformed config and absent/disabled fallback. Preserve preferences and existing hooks/settings. Handler/request JSON alone is not proof of actual MCP delivery. See [PR #6 evidence](evidence/PR6-Prism.md). |
| DoughTracker disposable creation trial — T04–T06/T12 | Build a backend slice in a disposable copy using DoughTracker's active contracts and the owner's requested coding participation. Inspect generated code/comments/docs and run actual behavior checks with trial-local resources. Record supplied authorship/help/observations, retain evaluation notes/check results and discard trial implementation/outputs/resources. Verify original files, Git state, uncommitted work and project resources are unchanged; no generated patch is applied. |
| Stafr source trial — T12/T18 | Inspect the existing Crew Workforce backend and explain actual request/data flow with concrete references. Preserve source/service state and use disposable copies for checks when needed. Architecture documents alone do not prove execution behavior. |
| Actual use versus preflight — T12 | Simulated learner conduct, code correctness, native delivery and actual supplied human reasoning remain separate. No independent answer, coding contribution or understanding is invented; unavailable human observations stay pending. |
| Completion and scope — T12–T18 | Applicable component checks/evidence support each reported result. Cross-provider coverage is pending under existing OpenAI access; optional tooling has verified fallback. Core/adapter dependencies remain portable and private-path-free. M08 installation/publication is excluded. |

## Per-slice sequence

1. Read the handoff and select applicable T criteria before implementing.
2. Write checks only for meaningful contracts/regressions; use the actual entry
   point rather than an in-test reimplementation or exact-prose snapshot.
3. Implement the portion and immediately run its relevant executable checks.
4. Run its focused interaction and actual development-hook checks in an external
   fixture. M01 cannot complete from handler-only or policy-only tests.
5. Record results, failures, and pending checks; update docs to the real status.
6. Review the slice before calling it complete or advancing its milestone status.

Current adapter contract command:

```sh
python3 -m unittest discover -s tests -v
```

Run the independent C# checks against a completed generated candidate:

```sh
python3 fixtures/expense-summary/check.py /absolute/path/to/candidate --reserved
```

The helper runs a fresh .NET check project with a forced rebuild. See the fixture
README for the underlying commands and when to use reserved cases. The starter
is intentionally incomplete and fails. Actual results, corrections, and pending
coverage are recorded in the M01 evidence report; future criteria are not passes.

## Human use and later automation

After M01–M04 verification, try a small real task. Invite an unaided explanation
or a related prediction/debugging attempt, record assistance, and adjust based on
what was observed. A comprehension gap suggests more support, not necessarily a
defect in correct shipped code. Do not require a coding contribution where project
instructions assign implementation to the agent.

Marketplace packaging/other-user installation is final M08 and does not substitute
for these local product checks. Later, automate the same scenario/evidence contract
with isolated actors and an observer. This evaluation automation is separate from
M06's invoked task feedback; it does not collect a runtime learner ledger or switch
levels. Separate software authorship from evidence of human reasoning: agent-written
code can be independently reviewed by a human, while copied explanations cannot
establish independent reasoning. Larger pilots, delayed recall and public learning
claims require their own scoped plan.
