namespace ExpenseSummary;

public sealed record Expense(DateOnly Date, string Category, decimal Amount);
