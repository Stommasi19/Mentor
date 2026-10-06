# S01 agreed contract

Supply these decisions only after the learner selects the matching response card.
The independent checks implement this public contract, not hidden business rules.

- Match categories with ordinal, case-insensitive comparison. Do not trim
  whitespace or normalize categories. An empty category is a valid exact label.
- Include negative amounts as refunds that reduce the total. Do not round or
  convert through binary floating point; sum decimal values.
- Select the calendar month containing `month`, including its first day and
  excluding the next month's first day. The supplied date need not be day one.
  Every valid `DateOnly` month is supported, including December of year 9999.
- Empty inputs and no matches return `0m`. Do not mutate the supplied records.
- Inputs and their elements/categories are non-null. Null behavior is unspecified.

The agreed implementation must document the matching, refund, and month rules
in its public code contract, plus provide useful usage and verification docs.
