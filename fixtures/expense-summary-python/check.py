#!/usr/bin/env python3
"""Independent public-behavior checks against a disposable Python candidate."""
import argparse
from datetime import date
from decimal import Decimal
import importlib.util
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', type=Path)
    args = parser.parse_args()
    specification = importlib.util.spec_from_file_location('expense_candidate', args.candidate / 'expense_totals.py')
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    expense = module.Expense
    entries = [expense(date(2026, 4, 30), 'Food', Decimal('90')),
               expense(date(2026, 5, 1), 'Food', Decimal('10.10')),
               expense(date(2026, 5, 31), 'FOOD', Decimal('-2.05')),
               expense(date(2026, 6, 1), 'food', Decimal('70')),
               expense(date(2026, 5, 10), 'food ', Decimal('50')),
               expense(date(2026, 5, 12), '', Decimal('3.00'))]
    cases = [('month/refunds/boundaries', entries, 'food', date(2026, 5, 19), Decimal('8.05')),
             ('no trimming', entries, 'food ', date(2026, 5, 1), Decimal('50')),
             ('empty label', entries, '', date(2026, 5, 1), Decimal('3')),
             ('no match', entries, 'rent', date(2026, 5, 1), Decimal('0')),
             ('empty input', [], 'food', date(2026, 5, 1), Decimal('0')),
             ('first calendar month', [expense(date.min, 'food', Decimal('1'))], 'food', date.min, Decimal('1')),
             ('last calendar month', [expense(date.max, 'food', Decimal('2'))], 'food', date.max, Decimal('2')),
             ('year boundary', [expense(date(2025, 12, 31), 'food', Decimal('4')),
                                expense(date(2026, 1, 1), 'food', Decimal('8'))],
              'food', date(2025, 12, 15), Decimal('4'))]
    original = list(entries)
    for label, values, category, month, expected in cases:
        actual = module.total_for_category(iter(values), category, month)
        if not isinstance(actual, Decimal) or actual != expected:
            raise AssertionError(f'{label}: expected Decimal {expected}, got {actual!r}')
    if entries != original:
        raise AssertionError('candidate mutated its input')
    print(f'PASS: {len(cases)} independent expense cases and input preservation')
    return 0


if __name__ == '__main__':
    sys.exit(main())
