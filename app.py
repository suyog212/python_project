import json
import requests
from geopy.geocoders import Nominatim
from datetime import datetime,timezone

def get_weather(city_name):
    #getting longitude and latitude
    def get_long_lat(name):
        geolocator = Nominatim(user_agent="Project")
        location=geolocator.geocode(name)
        return [location.longitude,location.latitude]
    lat_long = get_long_lat(city_name)
    #API key
    api_key = "f9955666136632343aff2e4ca9d9c909"
    #API url to fetch data
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat="
    url = base_url + str(lat_long[0]) + "&lon="+ str(lat_long[1]) + "&exclude=minutely&appid=" + api_key
    #request object to fetch data from api
    # res = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat_long[0]}&lon={lat_long[1]}&exclude=minutely&appid={api_key}").json()4
    res = requests.get(url,timeout=100).json()
    # print(ConnectionRefusedError)
    #Creating and adding data to JSON file
    with open("data.json","w",encoding="UTF-8") as file:
        json.dump(res,file)
    file.close()

#try block to handle runtime errors
try:
    get_weather("London")
finally:
    print("Something went wrong")

#reading and filtering data
with open('data.json','r') as f:
    data = json.load(f)
print(str(data["current"]["dt"]))
dt_dict = data['current']
print(dt_dict)

for i,j in enumerate(data):
    print(f"{j}")
# for i,(j,h) in enumerate(dt_dict.items()):
#     if j != 'weather':
#         print(f"{j} = {h}")
#     else:
#         print("done")
time = datetime.fromtimestamp(data["current"]["dt"])

print(time)