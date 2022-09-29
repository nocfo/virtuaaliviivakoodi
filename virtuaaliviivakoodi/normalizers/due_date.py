from datetime import date


def normalize_due_date(due_date: date) -> str:
    """
    Normalized due date into length 6 string.
    e.g. 2022-02-02 > "220202"
    """

    return due_date.strftime("%y%m%d")
