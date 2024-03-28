import requests
from dotenv import dotenv_values

config = dotenv_values("../.env")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
PARAMS = {
    "lat": 42,
    "lon": 25,
    "appid": config.get("OWM_KEY"),
    "units": "metric",
    "mode": "json",
    "cnt": 4,
}

response = requests.get(ENDPOINT, PARAMS)
response.raise_for_status()
print(response.text)
weather_data = response.json()
for interval in weather_data["list"]:
    for segment in interval["weather"]:
        if segment["id"] < 700:
            print(f"Rain expected around {interval["dt_txt"].split(" ")[-1]}")
