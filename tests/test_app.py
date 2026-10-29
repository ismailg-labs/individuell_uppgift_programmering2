from unittest.mock import Mock, patch

import pytest
import requests

from application.app import app
from application.cities import city_exists
from application.data_analys import avr_temp, create_line_chart
from application.weather import get_days, get_weather


# Denna test testar funktionen som ska kolla att staden finns i vår dictiranry
@pytest.mark.parametrize("city, expected", [("Stockholm", True), ("Fakecity", False)])
def test_city_exists(city, expected):
    assert city_exists(city) == expected


# testar get_weather funktionen med mock utan internet
def test_get_weather():
    with patch("application.weather.requests.get") as mock_get:
        mock_response = Mock()

        mock_response.json.return_value = {"current": {"temperature_2m": 15.0}}

        mock_get.return_value = mock_response

        data = get_weather(59.33, 18.07)

        assert data == {"current": {"temperature_2m": 15.0}}


# testar vår get_weather fast nör den kastar ett timeout error
def test_get_weather_timeout():
    with patch("application.weather.requests.get") as mock_get:
        mock_get.side_effect = requests.Timeout

        data = get_weather(59.33, 18.07)

        assert data == {"error": "Kunde tyvärr inte hämta väderdata!"}


# denna funktion testar vårt api när den kastar http error
def test_get_weather_httperror():
    with patch("application.weather.requests.get") as mock_get:
        mock_get.side_effect = requests.HTTPError

        data = get_weather(59.33, 18.07)

        assert data == {"error": "Kunde tyvärr inte hämta väderdata!"}


# Testar get_days funktionen mot fast data
def test_get_days():
    data = {
        "daily": {
            "time": ["2026-10-25"],
            "temperature_2m_max": [12],
            "temperature_2m_min": [6],
            "precipitation_sum": [2],
        }
    }

    days = get_days(data)

    assert days[0]["max"] == 12


# skapar en client som vi kan använda i flera tester utan att flask behöver vara igång
@pytest.fixture
def client():
    return app.test_client()


# test mot flask index sidan
def test_index_flask_page(client):
    response = client.get("/")
    assert response.status_code == 200


# test mot om nån skriver fel city bör vi få 404
def test_city_invalid(client):
    response = client.get("/weather?city=testfakecity")
    assert response.status_code == 404


# test vår felhantering
# för om nån skriver ett url som inte är kopplad til nån route
def test_invalid_url(client):
    response = client.get("/randomurlblablabla")
    assert response.status_code == 404


# Test för pandas funktionen
@pytest.mark.parametrize("days, expected", [ ( [ {"max": 10}, {"max": 20}, {"max": 30} ], 20 ), ( [ {"max": 5}, {"max": 10}, {"max": 30} ], 15 ) ])
def test_avg_temp(days, expected):
    assert avr_temp(days) == expected


# Test för plotly linjediagram funktionen
def test_line_diagram():
    days = [
        {"date": "2026-10-25", "max": 10},
        {"date": "2026-10-26", "max": 12},
        {"date": "2026-10-27", "max": 14},
    ]

    linje = create_line_chart(days)

    assert "plotly" in linje.lower()


def test_weather_api_error(client):
    with patch("application.app.get_weather") as mock_weather:
        mock_weather.return_value = {"error": "Kunde tyvärr inte hämta väderdata!"}

        response = client.get("/weather?city=Stockholm")

        assert response.status_code == 503
        assert "Kunde tyvärr inte hämta väderdata!" in response.get_data(as_text=True)


def test_weather_missingg_daily(client):
    with patch("application.app.get_weather") as mock_weather:
        mock_weather.return_value = {"current": {"temperature_2m": 15}}

        response = client.get("/weather?city=Stockholm")

        assert response.status_code == 503
        assert "Kunde inte läsa väderprognosen..." in response.get_data(as_text=True)