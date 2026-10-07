"""Exercise starter. Implement the public contract before claiming completion."""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Iterable


@dataclass(frozen=True)
class Expense:
    date: date
    category: str
    amount: Decimal


def total_for_category(expenses: Iterable[Expense], category: str, month: date) -> Decimal:
    """Total ASCII-case-insensitive exact labels in the calendar month, including refunds."""
    raise NotImplementedError('Implement the agreed expense-total contract.')
