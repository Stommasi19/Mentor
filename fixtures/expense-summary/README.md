# Expense-summary fixture (S01, version 1)

This is a C#/.NET 9 exercise, not the Mentor core's implementation language.
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
