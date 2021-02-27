from exchangeratesapi.rates import Rates, HistoryRates
from exchangeratesapi.functions import _load_rates, _load_history, API
from datetime import date
import pytest


def test_rates_rates(mocker):
    mockreturn = {
        "rates": {"USD": 1.1},
        "base": "EUR",
        "date": date.today().strftime("%Y-%m-%d")
    }

    mocker.patch('exchangeratesapi.rates._load_rates', return_value=mockreturn)

    rates = Rates()
    with pytest.assume:
        assert rates.date == date.today().strftime("%Y-%m-%d")
        assert rates.base == "EUR"
        assert rates.rates == {"USD": 1.1}
        assert repr(rates) == f'Rates(date="{date.today().strftime("%Y-%m-%d")}", base="EUR")'
        assert rates["USD"] == 1.1


def test_rates_history(mocker):
    mockreturn = {
        "rates": {"2021-01-02": {"USD": 1.1}, "2021-01-29": {"USD": 1.2}},
        "base": "EUR",
        "start_at": "2021-01-01",
        "end_at": "2021-01-31"
    }

    mocker.patch('exchangeratesapi.rates._load_history', return_value=mockreturn)
    start_at = "2021-01-01"
    end_at = "2021-01-31"
    history = HistoryRates('2021-01-01', '2021-01-31')

    with pytest.assume:
        assert history.start_at == start_at
        assert history.end_at == end_at
        assert history.base == "EUR"
        assert history.rates() == {"2021-01-02": {"USD": 1.1}, "2021-01-29": {"USD": 1.2}}
        assert history.rates(date="2021-01-02") == {"USD": 1.1}
        assert history.rates(date="2021-02-01") == {}
        assert repr(history) == f'HistoryRates(start_at="{start_at}", end_at="{end_at}", base="EUR")'
        assert history["USD"] == {"2021-01-02": 1.1, "2021-01-29": 1.2}


def test_rates__load_rates(requests_mock):
    mockreturn = {
        "rates": {"USD": 1.1},
        "base": "EUR",
        "date": date.today().strftime("%Y-%m-%d")
    }

    requests_mock.get(f'{API}/latest', json=mockreturn)
    latest_rates = _load_rates()
    with pytest.assume:
        assert latest_rates["date"] == date.today().strftime("%Y-%m-%d")
        assert latest_rates["base"] == "EUR"
        assert latest_rates["rates"]["USD"] == 1.1


def test_rates__load_history(requests_mock):
    start_at = "2021-01-01"
    end_at = "2021-01-31"
    mockreturn = {
        "rates": {"2021-01-02": {}, "2021-01-29": {}},
        "base": "EUR",
        "start_at": start_at,
        "end_at": end_at
    }

    requests_mock.get(f'{API}/history?start_at={start_at}&end_at={end_at}', json=mockreturn)
    history_rates = _load_history(start_at=start_at, end_at=end_at)
    with pytest.assume:
        assert history_rates["base"] == "EUR"
        assert history_rates["start_at"] == start_at
        assert history_rates["end_at"] == end_at
