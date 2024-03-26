import requests
import time
from datetime import datetime

LAT = 42
LONG = 25
DISTANCE = 4


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (abs(LAT - iss_latitude) < DISTANCE and
            abs(LONG - iss_longitude) < DISTANCE)


def is_dark_hours():
    parameters = {
        "lat": LAT,
        "lng": LONG,
        "formatted": 0,
        "tzid": "Europe/Sofia",
    }

    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now_hour = datetime.now().hour
    print((sunrise_hour, sunset_hour, time_now_hour))
    return time_now_hour < sunrise_hour or time_now_hour >= sunset_hour


while True:
    is_close = is_iss_close()
    is_dark = is_dark_hours()
    print(f"is_close:{is_close} is_dark:{is_dark}")
    if is_dark and is_close:
        print("Can be seen")
    time.sleep(60)
