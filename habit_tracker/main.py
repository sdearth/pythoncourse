import requests
from datetime import datetime

USERNAME = "sdfilter"
TOKEN = "thisismytoken"
GRAPH_ID = "cycling"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=parameters)
# response.raise_for_status()
# print(response.json())

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Cycling",
    "unit": "KM",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# response = requests.post(graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

graph_parameters = {
    "date": datetime.now().strftime("%Y%d%m"),
    "quantity": "10"
}
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
print(response.text)