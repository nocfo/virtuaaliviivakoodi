import decimal
import math
from typing import Tuple, Union


def split_euros_and_cents(
    euro_amount: Union[float, int, decimal.Decimal]
) -> Tuple[int, int]:
    cents_as_float, euros_as_float = math.modf(euro_amount)
    full_cents = int(round(cents_as_float * 100))
    full_euros = int(euros_as_float)
    return full_euros, full_cents
