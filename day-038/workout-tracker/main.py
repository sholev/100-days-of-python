import requests
import json
from datetime import datetime, timedelta
from dotenv import dotenv_values
import workouts_sheet

config = dotenv_values("../../.env")
host = "https://trackapi.nutritionix.com"
endpoint_nutrients = "/v2/natural/nutrients"
endpoint_exercise = "/v2/natural/exercise"

url_nutrients = f"{host}{endpoint_nutrients}"
url_exercise = f"{host}{endpoint_exercise}"

headers = {
    "Content-Type": "application/json",
    "x-app-id": config["NUTRITIONIX_ID"],
    "x-app-key": config["NUTRITIONIX_KEY"],
}


def exercise(query: str):
    body = json.dumps({
        "query": query
    })

    r = requests.post(url_exercise, data=body, headers=headers)
    if r.status_code != 200:
        print(f"Error: {r.status_code}")
        print(r.text)
    else:
        return r.json()


def nutrients(query: str):
    body = json.dumps({
        "query": query
    })

    r = requests.post(url_nutrients, data=body, headers=headers)
    if r.status_code != 200:
        print(f"Error: {r.status_code}")
        print(r.text)
    else:
        return r.json()


# nutrients("grape")
data = exercise(input("What did you do for exercise?\n"))
exercises = data["exercises"]
date_now = datetime.now()
for exercise_data in reversed(exercises):
    print(exercise_data)
    exercise = exercise_data["name"].title()
    duration = int(exercise_data["duration_min"])
    calories = float(exercise_data["nf_calories"])
    date_now -= timedelta(minutes=duration)
    date = date_now.strftime("%d/%m/%Y")
    time = date_now.strftime("%H:%M:%S")
    workouts_sheet.insert(date, time, exercise, str(duration), str(calories))


