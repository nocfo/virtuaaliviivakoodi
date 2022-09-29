import re
from typing import Union

from virtuaaliviivakoodi.exceptions import InvalidReferenceException
from virtuaaliviivakoodi.utils import remove_whitespace

RF_REFERENCE_PATTERN = r"^RF[0-9]{3,23}$"
FI_REFERENCE_PATTERN = r"^[0-9]{4,20}$"


def validate_reference(reference: Union[str, int]) -> None:
    if not isinstance(reference, (str, int)):
        raise InvalidReferenceException("Invalid reference. Must be string or integer.")

    reference_ = remove_whitespace(str(reference))

    if re.match(FI_REFERENCE_PATTERN, reference_):
        return

    if re.match(RF_REFERENCE_PATTERN, reference_):
        return

    raise InvalidReferenceException(
        "Invalid reference. Must use Finnish or RF reference formats."
    )
