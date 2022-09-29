from datetime import date
from typing import Union

from virtuaaliviivakoodi.normalizers import (
    normalize_due_date,
    normalize_euro_amount,
    normalize_iban,
    normalize_reference,
)
from virtuaaliviivakoodi.utils import detect_symbol_version
from virtuaaliviivakoodi.validators import (
    validate_due_date,
    validate_euro_amount,
    validate_iban,
    validate_reference,
)


def virtuaaliviivakoodi(
    iban: str,
    reference: Union[int, str],
    euro_amount: Union[float, int],
    due_date: date,
) -> str:
    """Generates virtuaaliviivakoodi's based on Pankkiviivakoodi opas spec
    https://www.finanssiala.fi/wp-content/uploads/2021/03/Pankkiviivakoodi-opas.pdf

    """

    validate_iban(iban)
    validate_reference(reference)
    validate_euro_amount(euro_amount)
    validate_due_date(due_date)

    return (
        detect_symbol_version(reference).value
        + normalize_iban(iban)
        + normalize_euro_amount(euro_amount)
        + normalize_reference(reference)
        + normalize_due_date(due_date)
    )
