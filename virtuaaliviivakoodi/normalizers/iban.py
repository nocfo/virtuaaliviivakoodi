from virtuaaliviivakoodi.utils import remove_whitespace


def normalize_iban(iban: str) -> str:
    """Normalizes IBAN by removing whitespace and stripping country code"""
    return remove_whitespace(iban)[2:]
