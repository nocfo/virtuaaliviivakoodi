from datetime import date, datetime
from typing import Union

from virtuaaliviivakoodi.constants.virtuaaliviivakoodi_slice import (
    VirtuaaliviivakoodiSlice,
)


def deconstruct_date(virtuaaliviivakoodi: str) -> Union[date, None]:
    """Deconstructs the due date from virtuaaliviivakoodi from "yymmdd" to datetime object.

    The date can be not defined, in which case it is "000000" in the virtuaaliviivakoodi.
    In this case None is returned.
    """

    due_date = virtuaaliviivakoodi[VirtuaaliviivakoodiSlice.DATE]

    if due_date == "000000":
        return None

    parsed_date = datetime.strptime(due_date, "%y%m%d").date()

    # CASE: Virtuaaliviivakoodi's date is over the year 69
    # Python's datetime assumes the year to be in the 1900s.
    # > Need to manually validate that the year is in the current century.
    # This is what you get for using 2-digit years.
    if parsed_date.year < 2000:
        parsed_date = parsed_date.replace(year=parsed_date.year + 100)

    return parsed_date
