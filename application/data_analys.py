import pandas as pd
import plotly.express as px


# funktionen som returnerar medelväde av kallaste temp för prognosdagarna
def avr_temp(days):
    temps = [day["max"] for day in days]

    return round(pd.Series(temps).mean(), 1)


# Funktion som skapar en plotly linjediagram över max temp för 3 dagarna
def create_line_chart(days):
    dates = [day["date"] for day in days]
    temps = [day["max"] for day in days]

    fig = px.line(x=dates, y=temps, markers=True)
    fig.update_layout(
        xaxis_title="Dag", yaxis_title="Temperatur i celsius", margin={"t": 10}
    )
    return fig.to_html(full_html=False)
