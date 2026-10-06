# Mentor verification plan

Status: M01's core, development adapter, fixture, executable checks, and local runs
are implemented. [M01 results](evidence/M01.md) cover T01–T05, T12, and T13
architecture. [M02 results](evidence/M02.md) on 2026-10-06 cover the required manual
control/preference contracts, native lifecycle/refresh, conduct simulations and
generated-code checks for the recorded combination. [M03 results](evidence/M03.md)
cover focused requirements, workflow invocation, mistake/direct-help and paused
conduct with independent generated-code checks. Automatic mid-turn compaction,
broader compatibility and human learning remain pending.
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
| S04 — review | A diff includes that boundary defect plus a harmless naming/style refinement. | Material defect reported with location/consequence; optional polish distinct; learner practices a supported review comment. |

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
| T06 | M02 | Guided scaffolds/offers coding, supported offers coding or review, independent permits delegation while the learner directs/reviews. | Repeat the same starting task under all three levels with fresh context. Judge conduct, not exact wording or line counts. |
| T07 | M02 | Session controls make no storage changes; explicit project changes persist. Projects remain separate, repo subdirectories/worktrees share settings, and updates preserve the other saved field. Status refresh retains local overrides and shows effective/saved values. | Real temporary roots/worktrees, hook/control round trips, fresh native sessions, and two already-open sessions with/without overrides. Include non-Git roots, symlinks, explicit data locations, and differing hook/tool cwd. |
| T08 | M02 | Pause removes compulsory teaching while retaining code standards. Missing state defaults; invalid state warns and stays intact until explicit reset. Failed writes/resets apply requested values locally with an unsaved warning. Project reset clears current overrides; other sessions retain their own. | Coaching-off S01 and control round trips with invalid/unsupported/unreadable state and unavailable/read-only storage. Confirm prior-record preservation, effective/saved values, and reset isolation. |
| T09 | M02, M03 | Mentor responds to the learner's mistake and offers increasingly useful help; a direct help request is honored. | S03 transcript and final behavioral check; no struggle quota or invented proficiency judgment. |
| T10 | M03 | Focused questions respond to learner reasoning, resolve what the next step needs, and record remaining assumptions. No mandatory rounds/delegation interview. | S02, one settled small task, and a direct-implementation request through the adapted workflow. |
| T11 | M04 | Actual diff/context read; identified material defect reported with evidence; optional polish separate; learner gets help forming a useful review comment. | S04 and an independent reproduction/check of its defect, plus coaching-off review. |
| T12 | All | Policy experiment, actual hook delivery, code quality/conduct/comprehension claims have the correct evidence; unperformed checks remain pending. | Inspect handback and cited artifacts. Neither policy-only runs nor synthetic actors prove automatic delivery or human learning. |
| T13 | M01 architecture; M05 coverage | Core has no target-language/vendor/host assumptions; compatibility claims reflect actual tests. | Inspect core/adapter boundary, then exercise representative languages and providers with the same rubric. Record a support matrix and pending cells. |
| T14 | M08 only | Verified core is packaged for others; discovery/install, trust, updates/removal, and release docs match supported behavior. | Final clean-environment distribution checks after local product/portability evidence. No early marketplace gate. |

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

Use the [M03 handoff](handoffs/M03-interview-coaching.md) for the focused scope.
Invoke the interview through the trusted hook guidance in an external workspace;
keep observer cards, independent checks, and other transcripts outside it.

| Boundary / criterion | Required observation |
| --- | --- |
| Local invocation — T02/T12/T13 architecture | Actual host receipt and model-visible guidance, followed by reading the canonical workflow from the pinned path. Execute guidance after checkout relocation/from another cwd; missing/empty/invalid resources fail visibly. No private toolkit or memory service is required. |
| Requirements — T10 | S02 questions follow uncertainty and scripted reasoning; month/refund/matching choices are recorded before code checks. Requirements-only requests do not edit code. Remaining assumptions and next-step verification stay visible. |
| Proportionate pacing — T10 | A fully specified small task proceeds without a compulsory interview or exercise, including on explicit invocation. Exercise the level-specific invitations without forcing code ownership. |
| Mistake/direct help — T09 | S03 inspects the actual boundary error, gives a useful hint, then honors requested direct help/takeover. Incorrect and corrected code are checked independently. |
| Paused/direct implementation — T08/T10 | Essential unresolved decisions are clarified while learning prompts are paused; a settled direct request receives complete checked code without an assignment. Effective/saved preferences stay distinct and unchanged unless explicitly requested. |
| Resulting code and evidence — T04/T12 | Review actual code/comments/docs, run independent checks, cite concrete transcript turns, and separate simulation, host delivery, software correctness, and observed human learning. |

Do not turn workflow prose into exact-wording tests. Existing process-boundary
adapter cases own invocation/quoting/resource failures; recorded conversations
assess conduct. Existing fixture checks own the agreed calculation contract.
Broader language/provider coverage and automatic adaptation remain later work.

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
with isolated actors and an observer. Test adaptive evidence separately from code authorship: agent-written
code can be independently reviewed by a human, while copied explanations cannot
establish independent reasoning. Larger pilots, delayed recall, and public
learning claims require their own scoped plan.
