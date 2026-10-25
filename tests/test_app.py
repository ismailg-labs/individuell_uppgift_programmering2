from application.cities import city_exists

# Denna test testar funktionen som ska kolla att staden finns i vår dictiranry
def test_city_exists():
    assert city_exists("Stockholm") == True
    assert city_exists("Fakecity") == False
