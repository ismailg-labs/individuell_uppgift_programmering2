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
### 1. Varför använder man mock i tester?
För att simulera ett anrop och kontrollera data utan att skicka ett riktigt anrop via internet.
På så sätt kan vi testa vår kod även om API:et är nere.

## 2. Varför använder man timeout och raise_for_status()?
För att dels inte vänta för evigt när man kör ett anrop samt för att fånga 4xx och 5xx fel såsom 500 till exempel

## 3. Vad är Jinja2 och varför används det?
Jinja2 kommer med flask automatiskt och gör att vi kan använda och visa pyhton data i HTML samt implementera logik i form av for loopar if else blocks.

## 4. Vad är en fixture i pytest?
En fixture i pytest används för att förbereda saker som flera tester behöver. I mitt projekt använder jag en fixture för att skapa en Flask test client som jag kan återanvända i flera tester.