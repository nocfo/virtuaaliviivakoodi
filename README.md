# Finnish virtuaaliviivakoodi generation

[![PyPI version](https://badge.fury.io/py/virtuaaliviivakoodi.svg)](https://badge.fury.io/py/virtuaaliviivakoodi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Virtuaaliviivakoodi is a Python library for generating and deconstructing virtual barcodes based on Finanssiala's [pankkiviivakoodi spec](https://www.finanssiala.fi/wp-content/uploads/2021/03/Pankkiviivakoodi-opas.pdf).

## Installation

```bash
pip install virtuaaliviivakoodi
```

## Usage

### Creating a virtual barcode

```python
from virtuaaliviivakoodi import virtuaaliviivakoodi

virtuaaliviivakoodi(
	iban="FI49 5000 9420 0287 30",
	reference="12345 67907",
	due_date=date(2022, 12, 12),
	euro_amount=100.20,
)

# > "449500094200287300001002000000000000001234567907201212"

```

### Deconstructing a virtual barcode

```python
from virtuaaliviivakoodi import deconstruct_virtuaaliviivakoodi

deconstruct = deconstruct_virtuaaliviivakoodi("449500094200287300001002000000000000001234567907201212")

# > deconstruct.symbol = SymbolVersion.VERSION_4,
#   deconstruct.iban = FI4950009420028730,
#   deconstruct.euro_amount = Decimal('100.20'),
#   deconstruct.reference = 1234567907,
#   deconstruct.due_date = date(2022, 12, 12),
```

## Function arguments

### Creating a virtual barcode

| Argument      | Type                    | Description                                                                                                                                                                                                   |
| ------------- |-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `iban`        | `str`                   | Mandatory. Payment receiver's IBAN. Must be in Finnish format. E.g.: `"FI49 5000 9420 0287 30"` or `"FI4950009420028730"`                                                                                     |
| `reference`   | `str` `int`             | Mandatory. Invoice reference in Finnish or international (RF) format. May invluce whitespace characters. E.g. `"12345 67907"`, `"1234567907"`, `1234567907` or `"RF92 1234 2345"`                             |
| `euro_amount` | `float` `int` `Decimal` | Mandatory. Invoice total amount in Euros. Must be positive number. According [the spec](https://www.finanssiala.fi/wp-content/uploads/2021/03/Pankkiviivakoodi-opas.pdf) amount must be smaller than 1000000. |
| `due_date`    | `date`                  | Optional. Invoice due date as a Python date object. If left empty, `"000000"` is used as the date according to [the spec](https://www.finanssiala.fi/wp-content/uploads/2021/03/Pankkiviivakoodi-opas.pdf)                                                                                       |

### Deconstructing a virtual barcode

| Argument              | Type                    | Description                                                                                                     |
|-----------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| `virtuaaliviivakoodi` | `str`                   | Mandatory. Virtuaaliviivakoodi to deconstruct. E.g.: `"449500094200287300001002000000000000001234567907201212"` |

## Exceptions

Exceptions can be imported the following way:

```python
from virtuaaliviivakoodi.exceptions import (
        VirtuaaliviivakoodiException,
        InvalidIBANException,
        InvalidReferenceException,
        InvalidEuroAmountException,
        InvalidDueDateException,
        InvalidSymbolException,
        InvalidLengthException
)
```

| Exception                      | Description                                                  |
|--------------------------------|--------------------------------------------------------------|
| `VirtuaaliviivakoodiException` | Base exception class for all of the following exceptions.    |
| `InvalidIBANException`         | Raised for invalid IBANs                                     |
| `InvalidReferenceException`    | Raised for invalid references                                |
| `InvalidEuroAmountException`   | Raised for invalid euro amounts                              |
| `InvalidDueDateException`      | Raised for invalid due dates                                 |
| `InvalidSymbolException`       | Raised for invalid symbol version of the virtuaaliviivakoodi |
| `InvalidLengthException`       | Raised for invalid length of the virtuaaliviivakoodi         |
