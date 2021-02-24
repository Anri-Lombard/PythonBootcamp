import os
import requests

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("API_KEY")
LATITUDE = -33.954071
LONGLITUDE = 18.475241

parameter = {
    "lat": LATITUDE,
    "lon": LONGLITUDE,
    "exclude": "current,daily,minutely",
    "appid": API_KEY,
}

response = requests.get(url=API_ENDPOINT, params=parameter)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in range(0, 12):
    if weather_data['hourly'][i]['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella for the rain today!")
else:
    print("Sky is clear, no need for an umbrella.")
