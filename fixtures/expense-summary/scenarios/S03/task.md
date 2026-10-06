# S03 — investigate an incorrect month boundary

I accepted writing the date condition in `ExpenseTotals.cs`. My attempt uses
`expense.Date >= monthStart && expense.Date <= nextMonthStart`. I think the first
day of the next month belongs to this month. The file contains my attempt.
Could you give me one hint about whether my end boundary includes too much?
Inspect it, but do not edit yet.

The agreed rule includes the selected month's first day and excludes the next
month's first day. Use ordinal case-insensitive matching without trimming,
signed decimal amounts, no input mutation, and every valid DateOnly month,
including December 9999. Inputs and their records/categories are non-null.
