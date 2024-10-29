from virtuaaliviivakoodi.constants.virtuaaliviivakoodi_slice import (
    VirtuaaliviivakoodiSlice,
)


def deconstruct_iban(virtuaaliviivakoodi: str) -> str:
    """Deconstructs the IBAN from virtuaaliviivakoodi"""

    return "FI" + virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.IBAN]
