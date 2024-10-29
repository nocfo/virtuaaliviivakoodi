from virtuaaliviivakoodi.exceptions import InvalidLengthException


def validate_length(virtuaaliviivakoodi: str) -> None:
    """Validates the lenght of the virtuaaliviivakoodi.

    The length of the virtuaaliviivakoodi must be 54 characters.
    """

    if len(virtuaaliviivakoodi) != 54:
        raise InvalidLengthException(
            "Invalid length of virtuaaliviivakoodi. Must be 54 characters."
        )
