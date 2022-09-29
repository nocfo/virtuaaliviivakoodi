class VirtuaaliviivakoodiException(Exception):
    pass


class InvalidIBANException(VirtuaaliviivakoodiException):
    pass


class InvalidReferenceException(VirtuaaliviivakoodiException):
    pass


class InvalidEuroAmountException(VirtuaaliviivakoodiException):
    pass


class InvalidDueDateException(VirtuaaliviivakoodiException):
    pass
