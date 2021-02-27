from exchangeratesapi.rates import latest, history
import pytest
from datetime import date


def test_latest(mocker):
    mockreturn = {
        "rates": {"USD": 1.1},
        "base": "EUR",
        "date": date.today().strftime("%Y-%m-%d")
    }

    mocker.patch('exchangeratesapi.rates._load_rates', return_value=mockreturn)
    latest_rates = latest()
    with pytest.assume:
        assert latest_rates["date"] == date.today().strftime("%Y-%m-%d")
        assert latest_rates["base"] == "EUR"
        assert latest_rates["rates"]["USD"] == 1.1


def test_history(mocker):
    mockreturn = {
        "rates": {"2021-01-02": {}, "2021-01-29": {}},
        "base": "EUR",
        "start_at": "2021-01-01",
        "end_at": "2021-01-31"
    }

    mocker.patch('exchangeratesapi.rates._load_history', return_value=mockreturn)
    start_at = "2021-01-01"
    end_at = "2021-01-31"
    history_rates = history('2021-01-01', '2021-01-31')
    with pytest.assume:
        assert history_rates["base"] == "EUR"
        assert history_rates["start_at"] == start_at
        assert history_rates["end_at"] == end_at