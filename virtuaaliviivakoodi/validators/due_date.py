from datetime import date

from virtuaaliviivakoodi.exceptions import InvalidDueDateException


def validate_due_date(due_date: date) -> None:
    if not isinstance(due_date, date):
        raise InvalidDueDateException("Due date must be date object")
