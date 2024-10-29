from datetime import date
from typing import Union


def normalize_due_date(due_date: Union[date, None]) -> str:
    """
    Normalized due date into length 6 string.
    e.g. 2022-02-02 > "220202"

    According to the documentation, the due date can be empty in which case 000000 is used.
    """

    return due_date.strftime("%y%m%d") if due_date else "000000"
