using ExpenseSummary;

// Expected totals are literal examples from the agreed public contract, not a
// second implementation of the filtering algorithm. Run outside the actor's copy.
var selectedMonth = new DateOnly(2026, 10, 17);
var cases = new List<(string Name, Expense[] Expenses, string Category, DateOnly Month, decimal Expected)>
{
    ("empty input", [], "Food", selectedMonth, 0m),
    ("no matching category", [new(new(2026, 10, 8), "Travel", 9m)], "Food", selectedMonth, 0m),
    ("case-insensitive matching", [new(new(2026, 10, 8), "fOoD", 3.25m)], "FOOD", selectedMonth, 3.25m),
    ("whitespace is significant", [new(new(2026, 10, 8), " Food ", 99m)], "Food", selectedMonth, 0m),
    ("refunds and decimal precision", [new(new(2026, 10, 8), "Food", 0.1m),
        new(new(2026, 10, 9), "Food", 0.2m), new(new(2026, 10, 10), "Food", -0.05m)],
        "Food", selectedMonth, 0.25m),
    ("small amount beside a large decimal", [new(new(2026, 10, 8), "Food", 9007199254740992m),
        new(new(2026, 10, 9), "Food", 0.01m), new(new(2026, 10, 10), "Food", -9007199254740992m)],
        "Food", selectedMonth, 0.01m),
    ("inclusive start and exclusive end", [new(new(2026, 9, 30), "Food", 100m),
        new(new(2026, 10, 1), "Food", 2m), new(new(2026, 10, 31), "Food", 4m),
        new(new(2026, 11, 1), "Food", 1000m)], "Food", selectedMonth, 6m),
    ("same month in another year", [new(new(2025, 10, 8), "Food", 100m),
        new(new(2026, 10, 8), "Food", 7m)], "Food", selectedMonth, 7m),
    ("ordinal comparison under Turkish culture", [new(new(2026, 10, 8), "BILLS", 5m),
        new(new(2026, 10, 8), "b\u0131lls", 100m)], "bills", selectedMonth, 5m),
};

// Reserved transfer cases: run only after the policy is stable. Their rules are
// public; these particular examples must not become input for prompt tuning.
if (args.Contains("--reserved"))
{
    cases.Add(("empty label across year boundary", [new(new(2026, 12, 31), "", 8m),
        new(new(2027, 1, 1), "", 100m)], "", new(2026, 12, 3), 8m));
    cases.Add(("last representable month", [new(new(9999, 12, 1), "Food", 2m),
        new(new(9999, 12, 31), "Food", 3m)], "Food", new(9999, 12, 15), 5m));
}

System.Globalization.CultureInfo.CurrentCulture = new("tr-TR");
var failures = 0;
foreach (var test in cases)
{
    try
    {
        var before = test.Expenses.ToArray();
        var actual = ExpenseTotals.TotalForCategory(test.Expenses, test.Category, test.Month);
        if (actual != test.Expected || !before.SequenceEqual(test.Expenses))
        {
            throw new Exception($"Expected {test.Expected}, got {actual}; input must remain unchanged.");
        }
        Console.WriteLine($"PASS: {test.Name}");
    }
    catch (Exception error)
    {
        failures++;
        Console.Error.WriteLine($"FAIL: {test.Name}: {error.Message}");
    }
}

Console.WriteLine($"{cases.Count - failures}/{cases.Count} behavioral checks passed.");
return failures == 0 ? 0 : 1;
