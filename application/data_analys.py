import pandas as pd
import plotly.express as px

# funktionen som returnerar medelväde av kallaste temp för prognosdagarna
def avr_temp(days):
    temps = [day["max"] for day in days]

    return round(pd.Series(temps).mean(), 1)