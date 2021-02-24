import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -33.954071
MY_LONG = 18.475241
MY_EMAIL = "anrihappybirthday@gmail.com"
MY_PASSWORD = "HappyBirthday"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

lat_vicinity = -38 < iss_latitude < -28
long_vicinity = 13 < iss_longitude < 23

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

is_night = sunset < time_now < sunrise

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if lat_vicinity and long_vicinity and is_night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="anri.m.lombard@gmail.com",
                msg="Subject:It is the ISS!\n\nLook up!",
            )




