import decimal

from virtuaaliviivakoodi.constants.virtuaaliviivakoodi_slice import (
    VirtuaaliviivakoodiSlice,
)


def deconstruct_amount(virtuaaliviivakoodi: str) -> decimal.Decimal:

    euros = virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.AMOUNT_EUROS]
    cents = virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.AMOUNT_CENTS]

    return decimal.Decimal(f"{euros}.{cents}")
