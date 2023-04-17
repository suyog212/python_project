import json
import requests
from geopy.geocoders import Nominatim
from datetime import datetime,timezone,timedelta

#API key
api_key = "f9955666136632343aff2e4ca9d9c909"

time_now = datetime.now() - timedelta(days=4)

#getting longitude and latitude
def get_long_lat(name):
        geolocator = Nominatim(user_agent="Project")
        location=geolocator.geocode(name)
        return [location.longitude,location.latitude]


def get_weather(city_name):
    lat_long = get_long_lat(city_name)
    #API url to fetch data
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat="
    url = base_url + str(lat_long[0]) + "&lon="+ str(lat_long[1]) + "&exclude=minutely&appid=" + api_key
    #request object to fetch data from api
    # res = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat_long[0]}&lon={lat_long[1]}&exclude=minutely&appid={api_key}").json()
    res = requests.get(url,timeout=100).json()
    # print(ConnectionRefusedError)
    #Creating and adding data to JSON file
    """json.dumps() function will convert a subset of Python objects into a json string.
    Not all objects are convertible and you may need to create a dictionary
    of data you wish to expose before serializing to JSON."""
    with open("data.json","w",encoding="UTF-8") as file:
        json.dump(res,file)
    file.close()

get_weather("London")

#reading and filtering data
with open('data.json','r') as f:
    data = json.load(f)
# print(str(data["current"]["dt"]))
dt_dict = data['current']
# print(dt_dict)
w_time = ["current","hourly","daily"]
for i in w_time:
    with open(f"{i}.json","w") as sorted_data:
        json.dump(data[i],sorted_data)

def weather_history(time_from,city_name):
    lat_long = get_long_lat(city_name)
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat_long[0]}&lon={lat_long[1]}&dt={time_from}&appid={api_key}"
    response = requests.get(url).json()
    print(response)

weather_history(datetime.timestamp(time_now),"London")

print("add hello")