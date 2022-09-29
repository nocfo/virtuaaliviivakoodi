from typing import Union

from virtuaaliviivakoodi.exceptions import InvalidEuroAmountException


def validate_euro_amount(euro_amount: Union[float, int]) -> None:
    if not isinstance(euro_amount, (float, int)):
        raise InvalidEuroAmountException("Euro amount must be float or integer value")

    if euro_amount < 0:
        raise InvalidEuroAmountException(
            "Invalid euro amount. Amount must be positive."
        )

    if euro_amount > 999999.99:
        raise InvalidEuroAmountException("Invalid euro amount. Max value is 999999.99")
