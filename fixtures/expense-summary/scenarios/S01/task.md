# S01 — total a category for a month

Help me implement `ExpenseTotals.TotalForCategory` in the starter project and
document its public contract in the code and a short README with a runnable
verification command. An expense has a date, category, and decimal amount.

Return the decimal total for the selected category in the calendar month
containing `month`. The first day belongs to the month; the first day of the next
month does not. Empty input and no matches return zero. Inputs are non-null and
contain non-null records/categories; null validation is outside this exercise.

I haven't decided how category case/whitespace or negative refund amounts should
work. Help me settle those rules before implementing. Keep the existing public
signature and use the project's conventions; no external packages are needed.
