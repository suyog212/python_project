import datetime as dt
import requests
from geopy.geocoders import Nominatim
import json


def get_long_lat(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city_name)
    return [location.longitude,location.latitude]

BASE_URL = "http://api.weatherapi.com/v1/history.json?key=&q=London&dt=2010-01-01"
API_KEY = "f9955666136632343aff2e4ca9d9c909"
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

res = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=minutely&appid={API_KEY}").json()

# js_data = json.dumps(res)

with open("data.json","w") as file:
    json.dump(res,file)

file.close()

print("Done !!!!!")
print("HEllo Suyog!")
print(get_long_lat("London")[0])
