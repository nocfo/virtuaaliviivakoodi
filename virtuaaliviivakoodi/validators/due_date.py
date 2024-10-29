from datetime import date
from types import NoneType
from typing import Union

from virtuaaliviivakoodi.exceptions import InvalidDueDateException


def validate_due_date(due_date: Union[date, None]) -> None:

    if not isinstance(due_date, (date, NoneType)):
        raise InvalidDueDateException("Due date must be date object")
