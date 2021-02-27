# pyexchangeratesapi

This is an unofficial Python wrapper for free [ExchangeRatesAPI](https://github.com/exchangeratesapi/exchangeratesapi), which provides exchange rate lookups courtesy of the [Central European Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html). It features a number of useful functions and can be installed easily using [pip](https://pypi.org/project/pip/).
Additionally wrapper is providing CLI interface. 

[![Test](https://github.com/jsporna/pyexchangeratesapi/workflows/Test/badge.svg)](https://github.com/jsporna/pyexchangeratesapi/actions?query=workflow%3ATest)
[![PyPI version](https://badge.fury.io/py/exchangeratesapi.svg)](https://badge.fury.io/py/exchangeratesapi)
![GitHub](https://img.shields.io/github/license/jsporna/pyexchangeratesapi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/exchangeratesapi)

[![codecov](https://codecov.io/gh/jsporna/pyexchangeratesapi/branch/main/graph/badge.svg?token=IF6K8NPW1Q)](https://codecov.io/gh/jsporna/pyexchangeratesapi)
[![Known Vulnerabilities](https://snyk.io/test/github/jsporna/pyexchangeratesapi/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/jsporna/pyexchangeratesapi?targetFile=requirements.txt)
[![CodeFactor](https://www.codefactor.io/repository/github/jsporna/pyexchangeratesapi/badge)](https://www.codefactor.io/repository/github/jsporna/pyexchangeratesapi)


## Installation

```shell
pip install exchangeratesapi
```

## Python usage

```python
from exchangeratesapi import rates

latest = rates.latest()
latest["base"]
latest["date"]

latest = rates.Rates()
latest.base
latest.date

history = rates.history(start_at="2020-01-01", end_at="2020-12-31", base="PLN")
history["base"]
history["start_at"]
history["end_at"]

history = rates.HistoryRates(start_at="2020-01-01", end_at="2020-12-31", base="PLN")
history.base
history.start_at
history.end_at
```