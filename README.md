# Hej Dennis! :) Nedan hittar du all info för att komma igång!

## Beskrivning
Detta är en väderapp byggd med Python och Flask :)

User kan välja mellan 5 städer i sverige och se vädret för dagen samt tredagarsprognos.

Data hämtas från Open-Meteo API.

## Installation guide

1. Clone repo från github
2. Skapa och aktivera venv miljö
3. Installera allt som behövs

```bash
pip install -r requirements-dev.txt
```

## Starta programmet
```bash
python -m application.app
```

Öppna sedan adressen som du ser i terminalen

## Tester
Testerna använder mock och pytest för att testa olika funktioner utan internet.

```bash
python -m pytest
```

## Ruff
Ruff används för att kontrollera kod och formatering.
```bash
ruff check .
ruff format --check .
```

## Tekniker (vad används i denna projekt)
- Python
- Flask och jinja2
- Requests
- Open Meteo API
- Pytest och Mock samt patch
- Pandas och plotly
- Bootstrap

## Teorifrågor som man ska beskvara
## 1. Varför mockar du anropen mot API:et i dina tester, och vad skulle hända om du inte gjorde det?
Jag använder mock i mina tests för att simulera/fejka svar från api utan att göra riktigt anrop. I `test_get_weather()` function använder jag
`patch` för att för att ersätta `requests.get`. Utan mocking skulle test behöva internet och kan misslykas om API ligger nere eller svarar på annat sätt än
förväntat

## 2. Vad gör timeout och raise_for_status(), och varför behövs de?
I min `get_weather()` funktion använder jag `timeout=10` för att inte vänta för länge på ett svar från api.
`raise_for_status()` kollar om http svaret inehåller fel 4xx eller 5xx och kastar undantag då som vi kan fånga.
Båda bahövs för att fånga api problem som kan uppstå och visa error istället för krascha.

## Hur fungerar mallarv i Jinja2? Förklara med exempel från dina egna mallar.
Mallarv inebär att flera html filer kan återanvända en gemensam basmall istället för att behöva skriva samma kod i varje html fil.
I min projekt använder jag `base.html` som inehåller grunden till sidorna. Mina anda html filer som exempelvisst `index.html` använder i sin html
`{% extends "base.html" %}` och fyller `{% block content %}` och title med sina egna inehåll.

## 4. Vad är en fixture, och vilken använder du?
En fixture i pytest används för att förbereda något som flera andra test behöver då slipper man skriva samma kod för varje test.
I min projekt har jag en fixture som heter client och skapar en flask test client med `app.test_client()`. Den använder jag i mina tester för att testa routes
utan att starta servern påriktigt.