namespace ExpenseSummary;

public static class ExpenseTotals
{
    public static decimal TotalForCategory(
        IEnumerable<Expense> expenses, string category, DateOnly month)
    {
        var monthStart = new DateOnly(month.Year, month.Month, 1);
        var isLastMonth = month.Year == 9999 && month.Month == 12;
        var nextMonthStart = isLastMonth ? DateOnly.MaxValue : monthStart.AddMonths(1);
        decimal total = 0m;

        foreach (var expense in expenses)
        {
            if (expense.Date >= monthStart && expense.Date <= nextMonthStart
                && string.Equals(expense.Category, category, StringComparison.OrdinalIgnoreCase))
            {
                total += expense.Amount;
            }
        }

        return total;
    }
}
