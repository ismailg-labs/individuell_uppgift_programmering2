from flask import Flask, render_template, request
from cities import cities, city_exists
from weather import get_weather, get_days

app = Flask(__name__, template_folder="templates")

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

    return render_template("weather.html",city=city, data=data, days=days)

@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)