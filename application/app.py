from flask import Flask, render_template, request
from application.cities import cities, city_exists
from application.weather import get_weather, get_days
from application.data_analys import avr_temp, create_line_chart

app = Flask(__name__, template_folder="templates")

@app.template_filter("uppercase")
def uppercase(text):
    return text.upper()


@app.route("/")
def index_page():
    return render_template("index.html", cities=cities)

@app.route("/weather")
def weather_page():
    city = request.args.get("city")

    if not city_exists(city):
        return render_template("404.html"), 404

    latitude, longitude = cities[city]
    data = get_weather(latitude, longitude)

    if "error" in data:
        return render_template("weather.html", error=data["error"])

    days = get_days(data)
    avrage = avr_temp(days)
    linje = create_line_chart(days)

    return render_template("weather.html",city=city, data=data, days=days, avrage=avrage, linje=linje)

@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404




if __name__ == "__main__":
    app.run(debug=True)