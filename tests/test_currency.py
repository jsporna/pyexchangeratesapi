from exchangeratesapi.currency import Currency
import pytest


def test_currency_eur():
    with pytest.assume:
        assert Currency.EUR.value == 0
        assert Currency.EUR.name == "EUR"
