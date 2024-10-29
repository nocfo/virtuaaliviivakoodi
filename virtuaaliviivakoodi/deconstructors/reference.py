from virtuaaliviivakoodi.constants import SymbolVersion
from virtuaaliviivakoodi.constants.virtuaaliviivakoodi_slice import (
    VirtuaaliviivakoodiSlice,
)
from virtuaaliviivakoodi.exceptions import InvalidSymbolException


def deconstruct_reference_and_version(
    virtuaaliviivakoodi: str,
) -> tuple[str, SymbolVersion]:
    """Returns the reference number in a human-readable format
    and the version of the virtuaaliviivakoodi"""

    reference: str
    symbol_version: SymbolVersion

    version = virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.SYMBOL]

    if version not in [version.value for version in SymbolVersion]:
        raise InvalidSymbolException("Invalid symbol version. Must be 4 or 5.")

    if version == SymbolVersion.VERSION_4.value:
        reference = virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.REFERENCE_FIN].lstrip(
            "0"
        )
        symbol_version = SymbolVersion.VERSION_4
    elif version == SymbolVersion.VERSION_5.value:
        reference = (
            "RF"
            + virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.REFERENCE_RF_HEAD]
            + virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.REFERENCE_RF_TAIL].lstrip(
                "0"
            )
        )
        symbol_version = SymbolVersion.VERSION_5

    return reference, symbol_version
