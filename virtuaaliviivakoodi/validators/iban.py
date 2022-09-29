import re

from virtuaaliviivakoodi.exceptions import InvalidIBANException
from virtuaaliviivakoodi.utils import remove_whitespace

FI_IBAN_REGEX = r"^FI\d{16}$"


def validate_iban(iban: str) -> None:
    if not isinstance(iban, str):
        raise InvalidIBANException("IBAN must be string")

    iban_ = remove_whitespace(iban)

    if not iban_.startswith("FI"):
        raise InvalidIBANException("IBAN must be Finnish")

    if not re.match(FI_IBAN_REGEX, iban_):
        raise InvalidIBANException("Invalid IBAN")
