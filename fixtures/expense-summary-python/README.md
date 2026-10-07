# Independent Python expense fixture

Copy `starter/` into a disposable workspace; the unfinished starter must fail.
Implement `total_for_category(expenses, category, month)` using Python `Decimal`.
Categories are ASCII labels compared case-insensitively without trimming; empty
labels are valid. Sum matching amounts in the supplied date's calendar month,
including negative refunds. Support the full `date` range, empty/no-match inputs
and iterable inputs without mutating records. Non-null/type-correct inputs are
assumed. Non-ASCII matching is outside this fixture's contract; Python casefold
and C# ordinal casing are not claimed equivalent for arbitrary Unicode.

Generate readable names/flow, useful comments explaining intent/non-obvious rules,
public-contract docs and usage/check instructions. Assess these separately from
behavior. Keep observer checks outside the learner workspace:

```sh
python3 fixtures/expense-summary-python/check.py /absolute/disposable/candidate
```

The checks use explicit independently chosen expected results. This standalone
fixture does not set Mentor's coding language or establish cross-provider support.
Agent-authored candidate results and scripted behavior establish no human learning.
