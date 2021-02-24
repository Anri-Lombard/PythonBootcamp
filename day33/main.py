import requests
import datetime as dt

MY_LONG = 18.475241
MY_LAT = -33.954071

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# data = response.json()
#
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = dt.datetime.now().hour
print(time_now)

night = int(sunset) < int(time_now) < int(sunrise)
day = int(sunrise) < int(time_now) < int(sunset)

print(day)










