from typing import Union

from virtuaaliviivakoodi.utils import split_euros_and_cents


def normalize_euro_amount(euro_amount: Union[float, int]) -> str:
    """
    Normalizes euro amount into length 8 string. E.g.
    123.23    > "00012323"
    123123.23 > "12312323"
    """
    euros, cents = split_euros_and_cents(euro_amount)
    euro_part = str(euros).zfill(6)
    cent_part = str(cents).zfill(2)

    return euro_part + cent_part
