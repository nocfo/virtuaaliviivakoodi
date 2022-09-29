from datetime import date
from unittest import TestCase

from parameterized import parameterized

from virtuaaliviivakoodi import virtuaaliviivakoodi
from virtuaaliviivakoodi.exceptions import (
    InvalidEuroAmountException,
    InvalidIBANException,
    InvalidReferenceException,
    VirtuaaliviivakoodiException,
)


class TestVirtuaaliviivakoodi(TestCase):
    @parameterized.expand(
        [
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "12 34561",
                    "euro_amount": 124.12,
                    "due_date": date(2022, 2, 2),
                },
                "449500094200287300001241200000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": 1234561,
                    "euro_amount": 124.12,
                    "due_date": date(2022, 2, 2),
                },
                "449500094200287300001241200000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "7777776",
                    "euro_amount": 2222.55,
                    "due_date": date(2020, 12, 12),
                },
                "449500094200287300022225500000000000000007777776201212",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "RF92 1234 2345",
                    "euro_amount": 2222.55,
                    "due_date": date(2020, 12, 12),
                },
                "549500094200287300022225592000000000000012342345201212",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "RF92 1234 2345",
                    "euro_amount": 999999.99,
                    "due_date": date(2020, 12, 12),
                },
                "549500094200287309999999992000000000000012342345201212",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "RF07999999999993",
                    "euro_amount": 0,
                    "due_date": date(2020, 12, 12),
                },
                "549500094200287300000000007000000000999999999993201212",
            ),
        ]
    )
    def test_valid_virtuaaliviivakoodis(self, options, expected_result):
        self.assertEqual(virtuaaliviivakoodi(**options), expected_result)

    @parameterized.expand(
        [
            (
                {
                    "iban": "   SE45 5000 0000 0583 9825 7466",
                    "reference": "12 34561",
                    "euro_amount": 124.12,
                    "due_date": date(2022, 2, 2),
                },
                InvalidIBANException,
                "IBAN must be Finnish",
            ),
            (
                {
                    "iban": "FI495000942002XXXX",
                    "reference": "7777776",
                    "euro_amount": 2222.55,
                    "due_date": date(2020, 12, 12),
                },
                InvalidIBANException,
                "Invalid IBAN",
            ),
            (
                {
                    "iban": 1234567,
                    "reference": "7777776",
                    "euro_amount": 2222.55,
                    "due_date": date(2020, 12, 12),
                },
                InvalidIBANException,
                "IBAN must be string",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": 12345.123,
                    "euro_amount": 2222.55,
                    "due_date": date(2020, 12, 12),
                },
                InvalidReferenceException,
                "Invalid reference. Must be string or integer.",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "INVALID REFERENCE",
                    "euro_amount": 2222.55,
                    "due_date": date(2020, 12, 12),
                },
                InvalidReferenceException,
                "Invalid reference. Must use Finnish or RF reference formats.",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "RF07999999999993",
                    "euro_amount": -1,
                    "due_date": date(2020, 12, 12),
                },
                InvalidEuroAmountException,
                "Invalid euro amount. Amount must be positive.",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "RF07999999999993",
                    "euro_amount": 1000000,
                    "due_date": date(2020, 12, 12),
                },
                InvalidEuroAmountException,
                "Invalid euro amount. Max value is 999999.99",
            ),
        ]
    )
    def test_invalid_virtuaaliviivakoodis(
        self, options, expected_exception, expected_error_message
    ):
        with self.assertRaises(expected_exception) as context:
            virtuaaliviivakoodi(**options)

        raised_exception = context.exception
        self.assertTrue(isinstance(raised_exception, VirtuaaliviivakoodiException))
        self.assertEqual(str(raised_exception), expected_error_message)
