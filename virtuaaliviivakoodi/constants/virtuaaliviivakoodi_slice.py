class VirtuaaliviivakoodiSlice:
    # fmt: off
    SYMBOL             = slice(0, 1)
    IBAN               = slice(1, 17)
    AMOUNT_EUROS       = slice(17, 23)
    AMOUNT_CENTS       = slice(23, 25)
    REFERENCE_FIN      = slice(28, 48)
    REFERENCE_RF_HEAD  = slice(25, 27)
    REFERENCE_RF_TAIL  = slice(27, 48)
    DATE               = slice(48, 54)
    # fmt: on
