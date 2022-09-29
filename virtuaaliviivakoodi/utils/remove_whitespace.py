import re


def remove_whitespace(str_in: str) -> str:
    str_out = re.sub(r"\s+", "", str_in)
    return str_out
