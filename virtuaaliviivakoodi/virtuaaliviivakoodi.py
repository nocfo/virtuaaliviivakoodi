import decimal
from datetime import date
from typing import Union

from virtuaaliviivakoodi.dataclasses import VirtuaaliviivakoodiDeconstruct
from virtuaaliviivakoodi.deconstructors import (
    deconstruct_amount,
    deconstruct_date,
    deconstruct_iban,
    deconstruct_reference_and_version,
)
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
    validate_length,
    validate_reference,
)


def virtuaaliviivakoodi(
    iban: str,
    reference: Union[int, str],
    euro_amount: Union[float, int, decimal.Decimal],
    due_date: date = None,
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


def deconstruct_virtuaaliviivakoodi(
    # pylint: disable=W0621
    virtuaaliviivakoodi: str,
) -> VirtuaaliviivakoodiDeconstruct:
    """Deconstructs virtuaaliviivakoodi into its parts.

    :param virtuaaliviivakoodi: Virtuaaliviivakoodi to deconstruct

    :return: VirtuaaliviivakoodiDeconstruct object containing
    the deconstructed parts of the virtuaaliviivakoodi
    """

    validate_length(virtuaaliviivakoodi)

    reference, symbol = deconstruct_reference_and_version(virtuaaliviivakoodi)
    iban = deconstruct_iban(virtuaaliviivakoodi)
    euro_amount = deconstruct_amount(virtuaaliviivakoodi)
    due_date = deconstruct_date(virtuaaliviivakoodi)

    return VirtuaaliviivakoodiDeconstruct(
        symbol=symbol,
        iban=iban,
        reference=reference,
        euro_amount=decimal.Decimal(euro_amount),
        due_date=due_date,
    )
