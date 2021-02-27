import requests
from datetime import datetime

app_id = "7cb27e58"
app_key = "92a426fc1fcf22868733752485fec160"
bearer_auth = f"Bearer Anrilombard22"

exercise_text = input("What exercise did you do? ")
my_gender = "male"
my_weight_in_kg = 72
my_height_in_cm = 170
my_age = 18

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://dashboard.sheety.co/projects/6039b2996f4f152d9d230ffa/sheets/workouts"

exercise_headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}
bearer_headers = {
    "Authorization": bearer_auth,
    "Content-Type": "application/json"
}

exercise_params = {
    "query": exercise_text,
    "gender": my_gender,
    "weight_kg": my_weight_in_kg,
    "height_cm": my_height_in_cm,
    "age": my_age
}

response = requests.post(exercise_endpoint, headers=exercise_headers, json=exercise_params)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
    sheet_response.raise_for_status()
    print(sheet_response.text)
    print(sheet_response.status_code)


