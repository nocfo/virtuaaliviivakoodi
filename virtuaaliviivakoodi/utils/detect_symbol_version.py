from typing import Union

from virtuaaliviivakoodi.constants import SymbolVersion


def detect_symbol_version(reference: Union[int, str]) -> SymbolVersion:
    reference_str = str(reference)

    if reference_str.startswith("RF"):
        return SymbolVersion.VERSION_5
    else:
        return SymbolVersion.VERSION_4
