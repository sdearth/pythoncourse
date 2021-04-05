import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# print((longitude, latitude))
parameters = {
    "lat": 35.9242942,
    "lng": -78.7826507,
    "formatted": 0
}
now = datetime.now()
response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
sunrise_time = sunrise.split("T")[1].split(":")[0]
sunset_time = sunset.split("T")[1].split(":")[0]
print(sunrise_time)
print(sunset_time)
print(now.hour)