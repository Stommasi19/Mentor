# Expense-summary fixture (S01–S03)

This is a C#/.NET 9 exercise, not the Mentor core's implementation language.
Spending is a sample coding domain for checking Mentor's conduct, not a Mentor
product feature. S01/S03 remain version 1; S02 requirements cards are version 2 (explicit skill, time box, concrete-plan confirmation).
`starter/` deliberately compiles but throws until the task is implemented.
An unfinished starter is not a passing generated-code result.

Copy only `starter/` and `scenarios/S01/task.md` to a disposable directory outside
Mentor, with no Mentor project instructions in its ancestry. Give the task to a
fresh session. Select replies from `response-cards.md` based on what it asks;
provide `agreed-contract.md` once those decisions are made. Keep the observer's
checks and other runs' transcripts outside the working copy. Shared filesystem
access means these runs are development simulations, not isolated actor studies.

Run the independent checks against the resulting project (Python 3.10+ and the
.NET 9 SDK; paths may contain spaces):

```sh
python3 fixtures/expense-summary/check.py "/absolute/path/to/candidate"
```

After stabilizing the policy, run the reserved transfer cases once:

```sh
python3 fixtures/expense-summary/check.py "/absolute/path/to/candidate" --reserved
```

The helper copies only the checks to a fresh temporary directory, then executes
`dotnet build <checks-project> --no-incremental -p:CandidateDirectory=<candidate>`
and `dotnet run --project <checks-project> --no-build` with the same property.
Rebuilding and separate outputs prevent one candidate's identically named
assembly from contaminating another run. Build artifacts also appear in the
disposable candidate. A failed build or check returns a nonzero exit code.

No test framework or third-party package is needed. The checks consume the public
API and use independently chosen expected values. The starter must fail them;
each finished candidate must pass. Read the generated code/comments/README as a
separate check of readability and documentation. Preserve actual diffs, selected
cards, settings, commands, and results outside public Git.

For S03, copy the starter and replace its `ExpenseTotals.cs` with
`scenarios/S03/ExpenseTotals.cs`, a deliberate inclusive-end mistake. Use that
scenario's task and response card for hint/direct-help behavior. Its incorrect
candidate must fail the next-month boundary checks; the corrected candidate must
pass. This simulated accepted contribution does not establish human learning.

For S02, copy the starter and `scenarios/S02/task.md` into an external workspace.
Keep `response-cards.md` and independent checks on the observer side. Select
replies based on actual questions; record the chosen month/refund/matching rules
before confirming the concrete plan, requesting implementation, and supplying
the shared agreed contract. Run
the same independent checks only after the concrete plan is confirmed and
implementation is authorized.
Also exercise a fully specified task and paused/direct implementation through
the interview workflow; neither should trigger a compulsory learning assignment.
