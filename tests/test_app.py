from application.cities import city_exists
import pytest
from unittest.mock import patch, Mock
from application.weather import get_weather, get_days
import requests

# Denna test testar funktionen som ska kolla att staden finns i vår dictiranry
@pytest.mark.parametrize("city, expected",[("Stockholm", True ), ("Fakecity", False)])
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
            "precipitation_sum": [2]}
    }

    days = get_days(data)

    assert days[0]["max"] == 12