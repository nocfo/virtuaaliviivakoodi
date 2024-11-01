import decimal
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
                    "reference": "12 34561",
                    "euro_amount": decimal.Decimal("124.12"),
                    "due_date": date(2022, 2, 2),
                },
                "449500094200287300001241200000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "12 34561",
                    "euro_amount": decimal.Decimal("0.01"),
                    "due_date": date(2022, 2, 2),
                },
                "449500094200287300000000100000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "12 34561",
                    "euro_amount": decimal.Decimal("999999.99"),
                    "due_date": date(2022, 2, 2),
                },
                "449500094200287309999999900000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI49 5000 9420 0287 30",
                    "reference": "12 34561",
                    "euro_amount": decimal.Decimal("0.00"),
                    "due_date": date(2022, 2, 2),
                },
                "449500094200287300000000000000000000000001234561220202",
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
            (
                {
                    "iban": "FI7944052020036082",
                    "reference": "868516259619897",
                    "euro_amount": 4883.15,
                    "due_date": date(2010, 6, 12),
                },
                "479440520200360820048831500000000868516259619897100612",
            ),
            (
                {
                    "iban": "FI5810171000000122",
                    "reference": "559582243294671",
                    "euro_amount": 482.99,
                    "due_date": date(2012, 1, 31),
                },
                "458101710000001220004829900000000559582243294671120131",
            ),
            (
                {
                    "iban": "FI0250004640001302",
                    "reference": "69875672083435364",
                    "euro_amount": 693.80,
                    "due_date": date(2011, 7, 24),
                },
                "402500046400013020006938000000069875672083435364110724",
            ),
            (
                {
                    "iban": "FI1566010001530641",
                    "reference": "7758474790647489",
                    "euro_amount": 7444.54,
                    "due_date": date(2019, 12, 19),
                },
                "415660100015306410074445400000007758474790647489191219",
            ),
            (
                {
                    "iban": "FI1680001400050267",
                    "reference": "78777679656628687",
                    "euro_amount": 935.85,
                },
                "416800014000502670009358500000078777679656628687000000",
            ),
            (
                {
                    "iban": "FI7331313001000058",
                    "reference": "868624",
                    "euro_amount": 0.00,
                    "due_date": date(2013, 8, 9),
                },
                "473313130010000580000000000000000000000000868624130809",
            ),
            (
                {
                    "iban": "FI8333010001100775",
                    "reference": "92125374252539897737",
                    "euro_amount": 150000.20,
                    "due_date": date(2016, 5, 25),
                },
                "483330100011007751500002000092125374252539897737160525",
            ),
            (
                {
                    "iban": "FI3936363002092492",
                    "reference": "590738390",
                    "euro_amount": 1.03,
                    "due_date": date(2023, 3, 11),
                },
                "439363630020924920000010300000000000000590738390230311",
            ),
            (
                {
                    "iban": "FI9239390001003391",
                    "reference": "1357914",
                    "euro_amount": 0.02,
                    "due_date": date(2099, 12, 24),
                },
                "492393900010033910000000200000000000000001357914991224",
            ),
            (
                {
                    "iban": "FI7944052020036082",
                    "reference": "RF09868516259619897",
                    "euro_amount": 4883.15,
                    "due_date": date(2010, 6, 12),
                },
                "579440520200360820048831509000000868516259619897100612",
            ),
            (
                {
                    "iban": "FI5810171000000122",
                    "reference": "RF06559582243294671",
                    "euro_amount": 482.99,
                    "due_date": date(2010, 1, 31),
                },
                "558101710000001220004829906000000559582243294671100131",
            ),
            (
                {
                    "iban": "FI0250004640001302",
                    "reference": "RF61698756720839",
                    "euro_amount": 693.80,
                    "due_date": date(2011, 7, 24),
                },
                "502500046400013020006938061000000000698756720839110724",
            ),
            (
                {
                    "iban": "FI1566010001530641",
                    "reference": "RF847758474790647489",
                    "euro_amount": 7444.54,
                    "due_date": date(2019, 12, 19),
                },
                "515660100015306410074445484000007758474790647489191219",
            ),
            (
                {
                    "iban": "FI1680001400050267",
                    "reference": "RF6078777679656628687",
                    "euro_amount": 935.85,
                    "due_date": None,
                },
                "516800014000502670009358560000078777679656628687000000",
            ),
            (
                {
                    "iban": "FI7331313001000058",
                    "reference": "RF10868624",
                    "euro_amount": 0.0,
                    "due_date": date(2013, 8, 9),
                },
                "573313130010000580000000010000000000000000868624130809",
            ),
            (
                {
                    "iban": "FI8333010001100775",
                    "reference": "RF7192125374252539897737",
                    "euro_amount": 150000.20,
                    "due_date": date(2016, 5, 25),
                },
                "583330100011007751500002071092125374252539897737160525",
            ),
            (
                {
                    "iban": "FI3936363002092492",
                    "reference": "RF66590738390",
                    "euro_amount": 1.03,
                    "due_date": date(2023, 3, 11),
                },
                "539363630020924920000010366000000000000590738390230311",
            ),
            (
                {
                    "iban": "FI9239390001003391",
                    "reference": "RF951357914",
                    "euro_amount": 0.02,
                    "due_date": date(2099, 12, 24),
                },
                "592393900010033910000000295000000000000001357914991224",
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
