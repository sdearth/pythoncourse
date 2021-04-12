from dotenv import load_dotenv
from datetime import datetime
import os
import requests


load_dotenv()

NUTRITIONIX_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
AGE = 52
WEIGHT = 73
HEIGHT = 183
GENDER = "male"

SHEETY_ENDPOINT = "https://api.sheety.co/bc15cdc12ffb9d77904fbedb497ae440/myWorkouts/workouts"

nutritionix_headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "x-remote-user-id": "0"
}

nutritionix_parameters = {
    "query": "",
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

sheety_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}",
    "Content-Type": "application/json"
}

query_string = input("What exercise did you do? ")

nutritionix_parameters["query"] = query_string

response = requests.post(
    url=NUTRITIONIX_ENDPOINT, 
    json=nutritionix_parameters, 
    headers=nutritionix_headers)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

sheety_data = {
    "workout": {
        "date": date,
        "time": time
    }
}

exercises = response.json()["exercises"]
for exercise in exercises:
    sheety_data["workout"]["exercise"] = exercise["name"]
    sheety_data["workout"]["duration"] = str(exercise["duration_min"])
    sheety_data["workout"]["calories"] = str(exercise["nf_calories"])

    response = requests.post(url=SHEETY_ENDPOINT,
        json=sheety_data,
        headers=sheety_headers)
