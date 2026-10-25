# De olika städerna och deras kordinatter hos apin (latitud, longitud)
cities = {
    "Stockholm": (59.33, 18.07),
    "Göteborg": (57.71, 11.97),
    "Malmö": (55.61, 13.00),
    "Umeå": (63.83, 20.26),
    "Kiruna": (67.86, 20.23)
}

# Funktion som kollar så att staden finns i vår dictionary
def city_exists(city):
    if city in cities:
        return True
    
    return False