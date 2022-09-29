from typing import Union

from virtuaaliviivakoodi.constants import SymbolVersion
from virtuaaliviivakoodi.utils import detect_symbol_version, remove_whitespace


def normalize_reference(reference: Union[str, int]) -> str:
    """Normalizes reference into 23 character string according to Pankkiviivakoodi-opas spec:
    https://www.finanssiala.fi/wp-content/uploads/2021/03/Pankkiviivakoodi-opas.pdf
    """
    reference_ = remove_whitespace(str(reference))
    symbol = detect_symbol_version(reference)

    if symbol == SymbolVersion.VERSION_5:
        return reference_[2:4] + reference_[4:].zfill(21)

    return reference_.zfill(23)
