import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "anri"
TOKEN = "Anrilombard22"
GRAPH_ID = "graph2"
hours = input("How many hours did you engineer value today?\n")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Engineering Graph",
    "unit": "Hours",
    "type": "int",
    "color": "sora"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

now = datetime.now()
date = now.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_params = {
    "date": date,
    "quantity": hours
}

# update_pixel_endpoint = f"{pixel_endpoint}/{date}"
# update_pixel_params = {
#     "quantity": "11"
# }

respone = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(respone.text)
