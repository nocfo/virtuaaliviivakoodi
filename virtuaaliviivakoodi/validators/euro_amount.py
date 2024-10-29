import decimal
from typing import Union

from virtuaaliviivakoodi.exceptions import InvalidEuroAmountException


def validate_euro_amount(euro_amount: Union[float, int, decimal.Decimal]) -> None:
    if not isinstance(euro_amount, (float, int, decimal.Decimal)):
        raise InvalidEuroAmountException(
            "Euro amount must be float, integer or decimal value"
        )

    if euro_amount < 0:
        raise InvalidEuroAmountException(
            "Invalid euro amount. Amount must be positive."
        )

    if euro_amount > decimal.Decimal("999999.99"):
        raise InvalidEuroAmountException("Invalid euro amount. Max value is 999999.99")
