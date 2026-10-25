import requests

# Hämtar väder från api där vi via params skcikar med allt vi vill ha info om 
# samt enkel felhanttering som kollar så att anropet gick bra
def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "forecast_days": 3
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException:
        return {"error": "Kunde tyvärr inte hämta väderdata!"}

    else:
        return data

