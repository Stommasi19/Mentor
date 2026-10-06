# Mentor verification plan

Status: Criteria specified; no plugin, fixtures, executable checks, or evaluation
runs have been implemented. Test each implemented portion immediately.
Scope and ownership: [IMPLEMENTATION-PLAN.md](IMPLEMENTATION-PLAN.md).

## Evidence and results

Use `pass`, `fail`, or `pending` per criterion. A pending host interaction is
not a pass; record the unavailable action or missing observation. For mentoring
judgments, use `inconclusive` when the transcript cannot support a conclusion.
Do not hide an actual defect inside an aggregate score.

| Evidence | Establishes |
| --- | --- |
| Hook execution and delivered context | The host loaded this installed policy. |
| Behavioral code checks | The resulting code satisfies the checked requirements. |
| Readability review of the actual diff | This change is understandable and documented appropriately. |
| Transcript observations with turn references | Mentor followed the relevant interaction criteria in this run. |
| Unaided human explanation, prediction, or diagnosis | Observed comprehension on that task; a small pilot does not establish a causal learning improvement. |

For a slice, record commit/package/host/model versions, settings, fixture/scenario
version, starting preferences, actual hook evidence, transcript turns, authored
contributions, final diff, commands/results, criterion judgments, and limitations.
Record failed runs too. Keep raw local transcripts outside public Git; publish
sanitized examples only through a separately requested release/demo task.

## Reusable fixture

Start with a tiny C# expense-summary project: records containing a date, category,
and decimal amount, plus a function that totals matching expenses. No database,
web server, real user data, or DoughTracker dependency is needed.

Add it during M01 and run from disposable copies outside Mentor. Version the
starter, public task, scripted learner response cards, and independent checks.
Record the actual .NET SDK/target. Restore the starter and a controlled preference
record before each run. Reuse the domain while changing the task and misconception.

| Scenario | Task | What to observe |
| --- | --- | --- |
| S01 — small implementation | Total a category; clarify matching semantics where necessary. | Useful decision/prediction, purposeful coding offer when selected, readable final code, takeover respected. |
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

For representative Mentor/baseline comparisons, hold model/settings, starter,
task, response profile, and unrelated plugins constant. Reset preferences/context.
Exclude Mentor policy from baseline hooks and project instructions, including
this repository's AGENTS.md. Baseline comparison informs evaluation; it is not
required for every unrelated implementation edit. Review disputed observer
judgments and a sample of successes manually.

## Criteria

| ID | Slice | Observable criterion | Immediate method |
| --- | --- | --- | --- |
| T01 | M01 | Package discovery/install works; actual trusted hook context arrives without manually invoking Mentor. Disabled/untrusted Mentor does not supply that context. | Fresh disposable workspace outside Mentor; capture host evidence and installed path/version. Inspect current host help/trust flow. |
| T02 | M01 | Hook emits valid event JSON and nonempty policy from its installed package when invoked from another directory; absent policy fails visibly. | Execute the real entry point with synthetic event input and packaged-resource failure; protect this executable contract. |
| T03 | M01, M02 | Each exercised startup/resume/clear/compact event reloads policy; stored preferences survive and explicit session choices are not reset by defaults. | Separate host lifecycle observations; handler event coverage alone does not prove runtime lifecycle delivery. |
| T04 | M01, M02 | Changed code has descriptive names, traceable flow, appropriate boundaries, and useful accurate comments/docs; unnecessary polish stays optional. | Inspect S01 final diff and explain an important rule/failure case; run the project's existing relevant checks. |
| T05 | M01, M02 | A learner coding offer is meaningful and conditional; demonstration/takeover or agent-implements project agreements receive complete work. | S01 with a decision/attempt and takeover variant; check authored contribution and actual completed code. |
| T06 | M02 | Guided scaffolds/offers coding, supported offers coding or review, independent permits delegation while the learner directs/reviews. | Repeat the same starting task under all three levels with fresh context. Judge conduct, not exact wording or line counts. |
| T07 | M02 | Explicit preferences persist; two projects remain separate; one repo's subdirectories/worktrees share settings; changing one field preserves the other. | Execute control helper and hook across temporary roots/worktrees plus subsequent fresh host sessions. Check non-Git root behavior. |
| T08 | M02 | Pause removes compulsory teaching while retaining code standards. Missing state defaults; invalid state warns without overwrite; failed storage does not claim persistence. | Hook/control round trips and coaching-off S01. Include reset of one project only and unavailable/read-only storage. |
| T09 | M02, M03 | Mentor responds to the learner's mistake and offers increasingly useful help; a direct help request is honored. | S03 transcript and final behavioral check; no struggle quota or invented proficiency judgment. |
| T10 | M03 | Focused questions respond to learner reasoning, resolve what the next step needs, and record remaining assumptions. No mandatory rounds/delegation interview. | S02, one settled small task, and a direct-implementation request through the adapted workflow. |
| T11 | M04 | Actual diff/context read; identified material defect reported with evidence; optional polish separate; learner gets help forming a useful review comment. | S04 and an independent reproduction/check of its defect, plus coaching-off review. |
| T12 | All | Runtime/code/readability/conduct/comprehension claims have the correct evidence; unperformed checks remain pending. | Inspect the slice handback and cited artifacts. Synthetic actors provide no human-learning result. |

T04 review questions:

- Can another developer trace the changed behavior and explain the names?
- Do boundaries and abstractions serve the current behavior?
- Do comments explain non-obvious reasons and docs reproduce actual verification?
- Does the code handle the agreed failure/boundary case, and do checks demonstrate it?

A readability review records a concrete example and any necessary correction.
Do not invent universal method-length limits, comment quotas, or subjective scores
as release gates. Disclose every identified material defect even when the
conversation concentrates on one learning topic.

## Per-slice sequence

1. Read the handoff and select applicable T criteria before implementing.
2. Write checks only for meaningful contracts/regressions; use the actual entry
   point rather than an in-test reimplementation or exact-prose snapshot.
3. Implement the portion and immediately run its relevant executable checks.
4. Run its focused interaction and actual host checks in an external fixture.
5. Record results, failures, and pending checks; update docs to the real status.
6. Review the slice before calling it complete or advancing its milestone status.

Planned Python command once tests exist:

```sh
python3 -m unittest discover -s tests -v
```

Record the fixture's actual C# check command when M01 creates it; run it against
the resulting code. No checks above have been performed by writing this plan.

## Human use and later automation

After M01–M04 verification, try a small real task. Invite an unaided explanation
or a related prediction/debugging attempt, record assistance, and adjust based on
what was observed. A comprehension gap suggests more support, not necessarily a
defect in correct shipped code. Do not require a coding contribution where project
instructions assign implementation to the agent.

Later, automate the same scenario/evidence contract with isolated actors and an
observer. Test adaptive evidence separately from code authorship: agent-written
code can be independently reviewed by a human, while copied explanations cannot
establish independent reasoning. Larger pilots, delayed recall, and public
learning claims require their own scoped plan.
