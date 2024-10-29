import decimal
from datetime import date
from unittest import TestCase

from parameterized import parameterized

from virtuaaliviivakoodi import deconstruct_virtuaaliviivakoodi
from virtuaaliviivakoodi.constants import SymbolVersion
from virtuaaliviivakoodi.exceptions import (
    InvalidLengthException,
    InvalidSymbolException,
)


class TestVirtuaaliviivakoodi(TestCase):
    @parameterized.expand(
        [
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "1234561",
                    "euro_amount": decimal.Decimal("124.12"),
                    "due_date": date(2022, 2, 2),
                    "version": SymbolVersion.VERSION_4,
                },
                "449500094200287300001241200000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "1234561",
                    "euro_amount": decimal.Decimal("124.12"),
                    "due_date": date(2022, 2, 2),
                    "version": SymbolVersion.VERSION_4,
                },
                "449500094200287300001241200000000000000001234561220202",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "7777776",
                    "euro_amount": decimal.Decimal("2222.55"),
                    "due_date": date(2020, 12, 12),
                    "version": SymbolVersion.VERSION_4,
                },
                "449500094200287300022225500000000000000007777776201212",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "RF9212342345",
                    "euro_amount": decimal.Decimal("2222.55"),
                    "due_date": date(2020, 12, 12),
                    "version": SymbolVersion.VERSION_5,
                },
                "549500094200287300022225592000000000000012342345201212",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "RF9212342345",
                    "euro_amount": decimal.Decimal("999999.99"),
                    "due_date": date(2020, 12, 12),
                    "version": SymbolVersion.VERSION_5,
                },
                "549500094200287309999999992000000000000012342345201212",
            ),
            (
                {
                    "iban": "FI4950009420028730",
                    "reference": "RF07999999999993",
                    "euro_amount": decimal.Decimal(0),
                    "due_date": date(2020, 12, 12),
                    "version": SymbolVersion.VERSION_5,
                },
                "549500094200287300000000007000000000999999999993201212",
            ),
            (
                {
                    "iban": "FI7944052020036082",
                    "reference": "868516259619897",
                    "euro_amount": decimal.Decimal("4883.15"),
                    "due_date": date(2010, 6, 12),
                    "version": SymbolVersion.VERSION_4,
                },
                "479440520200360820048831500000000868516259619897100612",
            ),
            (
                {
                    "iban": "FI5810171000000122",
                    "reference": "559582243294671",
                    "euro_amount": decimal.Decimal("482.99"),
                    "due_date": date(2012, 1, 31),
                    "version": SymbolVersion.VERSION_4,
                },
                "458101710000001220004829900000000559582243294671120131",
            ),
            (
                {
                    "iban": "FI0250004640001302",
                    "reference": "69875672083435364",
                    "euro_amount": decimal.Decimal("693.80"),
                    "due_date": date(2011, 7, 24),
                    "version": SymbolVersion.VERSION_4,
                },
                "402500046400013020006938000000069875672083435364110724",
            ),
            (
                {
                    "iban": "FI1566010001530641",
                    "reference": "7758474790647489",
                    "euro_amount": decimal.Decimal("7444.54"),
                    "due_date": date(2019, 12, 19),
                    "version": SymbolVersion.VERSION_4,
                },
                "415660100015306410074445400000007758474790647489191219",
            ),
            (
                {
                    "iban": "FI1680001400050267",
                    "reference": "78777679656628687",
                    "euro_amount": decimal.Decimal("935.85"),
                    "due_date": None,
                    "version": SymbolVersion.VERSION_4,
                },
                "416800014000502670009358500000078777679656628687000000",
            ),
            (
                {
                    "iban": "FI7331313001000058",
                    "reference": "868624",
                    "euro_amount": decimal.Decimal("0.00"),
                    "due_date": date(2013, 8, 9),
                    "version": SymbolVersion.VERSION_4,
                },
                "473313130010000580000000000000000000000000868624130809",
            ),
            (
                {
                    "iban": "FI8333010001100775",
                    "reference": "92125374252539897737",
                    "euro_amount": decimal.Decimal("150000.20"),
                    "due_date": date(2016, 5, 25),
                    "version": SymbolVersion.VERSION_4,
                },
                "483330100011007751500002000092125374252539897737160525",
            ),
            (
                {
                    "iban": "FI3936363002092492",
                    "reference": "590738390",
                    "euro_amount": decimal.Decimal("1.03"),
                    "due_date": date(2023, 3, 11),
                    "version": SymbolVersion.VERSION_4,
                },
                "439363630020924920000010300000000000000590738390230311",
            ),
            (
                {
                    "iban": "FI9239390001003391",
                    "reference": "1357914",
                    "euro_amount": decimal.Decimal("0.02"),
                    "due_date": date(2099, 12, 24),
                    "version": SymbolVersion.VERSION_4,
                },
                "492393900010033910000000200000000000000001357914991224",
            ),
            (
                {
                    "iban": "FI7944052020036082",
                    "reference": "RF09868516259619897",
                    "euro_amount": decimal.Decimal("4883.15"),
                    "due_date": date(2010, 6, 12),
                    "version": SymbolVersion.VERSION_5,
                },
                "579440520200360820048831509000000868516259619897100612",
            ),
            (
                {
                    "iban": "FI5810171000000122",
                    "reference": "RF06559582243294671",
                    "euro_amount": decimal.Decimal("482.99"),
                    "due_date": date(2010, 1, 31),
                    "version": SymbolVersion.VERSION_5,
                },
                "558101710000001220004829906000000559582243294671100131",
            ),
            (
                {
                    "iban": "FI0250004640001302",
                    "reference": "RF61698756720839",
                    "euro_amount": decimal.Decimal("693.80"),
                    "due_date": date(2011, 7, 24),
                    "version": SymbolVersion.VERSION_5,
                },
                "502500046400013020006938061000000000698756720839110724",
            ),
            (
                {
                    "iban": "FI1566010001530641",
                    "reference": "RF847758474790647489",
                    "euro_amount": decimal.Decimal("7444.54"),
                    "due_date": date(2019, 12, 19),
                    "version": SymbolVersion.VERSION_5,
                },
                "515660100015306410074445484000007758474790647489191219",
            ),
            (
                {
                    "iban": "FI1680001400050267",
                    "reference": "RF6078777679656628687",
                    "euro_amount": decimal.Decimal("935.85"),
                    "due_date": None,
                    "version": SymbolVersion.VERSION_5,
                },
                "516800014000502670009358560000078777679656628687000000",
            ),
            (
                {
                    "iban": "FI7331313001000058",
                    "reference": "RF10868624",
                    "euro_amount": decimal.Decimal("0.0"),
                    "due_date": date(2013, 8, 9),
                    "version": SymbolVersion.VERSION_5,
                },
                "573313130010000580000000010000000000000000868624130809",
            ),
            (
                {
                    "iban": "FI8333010001100775",
                    "reference": "RF7192125374252539897737",
                    "euro_amount": decimal.Decimal("150000.20"),
                    "due_date": date(2016, 5, 25),
                    "version": SymbolVersion.VERSION_5,
                },
                "583330100011007751500002071092125374252539897737160525",
            ),
            (
                {
                    "iban": "FI3936363002092492",
                    "reference": "RF66590738390",
                    "euro_amount": decimal.Decimal("1.03"),
                    "due_date": date(2023, 3, 11),
                    "version": SymbolVersion.VERSION_5,
                },
                "539363630020924920000010366000000000000590738390230311",
            ),
            (
                {
                    "iban": "FI9239390001003391",
                    "reference": "RF951357914",
                    "euro_amount": decimal.Decimal("0.02"),
                    "due_date": date(2099, 12, 24),
                    "version": SymbolVersion.VERSION_5,
                },
                "592393900010033910000000295000000000000001357914991224",
            ),
        ]
    )
    def test_valid_virtuaaliviivakoodis_deconstruct(
        self, expected_result, virtuaaliviivakoodi
    ):

        deconstruct = deconstruct_virtuaaliviivakoodi(virtuaaliviivakoodi)

        result = {
            "version": deconstruct.symbol,
            "iban": deconstruct.iban,
            "euro_amount": deconstruct.euro_amount,
            "reference": deconstruct.reference,
            "due_date": deconstruct.due_date,
        }

        self.assertEqual(result, expected_result)

    @parameterized.expand(
        [
            (
                "692393900010033910000000295000000000000001357914991224",
                InvalidSymbolException,
            ),
            (
                "392393900010033910000000295000000000000001357914991224",
                InvalidSymbolException,
            ),
            (
                "4923939000100339100000002950000000000001357914991224",
                InvalidLengthException,
            ),
            (
                "492393900010033910000000295000000000000000001357914991224",
                InvalidLengthException,
            ),
            (
                "492393900010033910000000295000000000000001357914999999",
                ValueError,
            ),
        ]
    )
    def test_invalid_virtuaaliviivakoodis_deconstruct(self, virtuaaliviivakoodi, error):
        with self.assertRaises(error):
            deconstruct_virtuaaliviivakoodi(virtuaaliviivakoodi)
