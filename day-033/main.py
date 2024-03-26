import requests
from datetime import datetime as dt
# import pprint


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# pprint.pp(vars(response))
pos = response.json()["iss_position"]
coord = (pos["longitude"], pos["latitude"])
print(coord)

params = {
    "lat": pos["latitude"],
    "lng": pos["longitude"],
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")
sunset = data["results"]["sunset"].split("T")
print(f"Sunrise: {sunrise}, Sunset: {sunset}")
