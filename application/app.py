from flask import Flask, render_template, request

from application.cities import cities, city_exists
from application.data_analys import avr_temp, create_line_chart
from application.weather import get_days, get_weather

# skapar själva appen och visar vart jinja2 hittar mallarna
app = Flask(__name__, template_folder="templates")

# egen jinja2 filter som gör texten till all upper case :)
@app.template_filter("uppercase")
def uppercase(text):
    return text.upper()


@app.route("/")
def index_page():
    return render_template("index.html", cities=cities)


# hämtar den stad som user vald och visar datan på sidan för den staden
@app.route("/weather")
def weather_page():
    city = request.args.get("city")

    if not city_exists(city):
        return render_template("404.html"), 404

    latitude, longitude = cities[city]
    data = get_weather(latitude, longitude)

    if "error" in data:
        return render_template("weather.html", error=data["error"]), 503
    
    # Hanterar om data saknas
    try:
        days = get_days(data)
    except ValueError:
        return render_template("weather.html", error="Kunde inte läsa väderprognosen..."), 503
    
    avrage = avr_temp(days)
    linje = create_line_chart(days)

    return render_template(
        "weather.html", city=city, data=data, days=days, avrage=avrage, linje=linje
    )

# tar hand om 404 http erros och slussar vidare till 404 html sidan.
@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404

# startar sjölva flask appen
if __name__ == "__main__":
    app.run(debug=True)
