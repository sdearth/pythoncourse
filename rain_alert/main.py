from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("APIKEY")
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LONG = "-78.8664"
LAT = "36.0335"
EXCLUDE="current,minutely,daily,alerts"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": EXCLUDE,
    "appid": api_key,
    "units": "imperial"
}

response = requests.get(url=ENDPOINT, params=parameters)

response.raise_for_status()

body = response.json()
#print(body["hourly"])
hourly_slice = body['hourly'][:12]

for hour in hourly_slice:
    weather_id = hour['weather'][0]['id']
    if weather_id < 700:
        print("bring an umbrella")
        break