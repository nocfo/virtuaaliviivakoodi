from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional

from virtuaaliviivakoodi.constants import SymbolVersion


@dataclass(frozen=True)
class VirtuaaliviivakoodiDeconstruct:
    symbol: SymbolVersion
    iban: str
    reference: str
    euro_amount: Decimal
    due_date: Optional[date]
