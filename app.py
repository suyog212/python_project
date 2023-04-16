import datetime as dt
import requests
from geopy.geocoders import Nominatim
import json

def get_weather(city_Name):
    #getting longitude and latitude
    def get_long_lat(city_name):
        geolocator = Nominatim(user_agent="Project")
        location=geolocator.geocode(city_name)
        return [location.longitude,location.latitude]
    
    lat_long = get_long_lat(city_Name)
    #API key
    API_KEY = "f9955666136632343aff2e4ca9d9c909"
    #API url to fetch data
    BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat="
    CITY = "London"
    url = BASE_URL + lat_long[0] + "&lon="+ lat_long[1] + "&exclude=minutely&appid=" + API_KEY
    #request object to fetch data from api
    # res = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat_long[0]}&lon={lat_long[1]}&exclude=minutely&appid={API_KEY}").json()4
    res = requests.get(url)
    #Creating and adding data to JSON file 
    with open("data.json","w") as file:
        json.dump(res,file)

    file.close()


get_weather("London")
print("Done !!!!!")