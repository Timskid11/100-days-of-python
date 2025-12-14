import requests
import datetime
import os

username = os.environ.get("1")
passw = os.environ.get("2")


basic = (username, passw)


APP_ID = "**********"

API_KEY = "**********************"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = "78"
HEIGHT_CM = "187.8"
AGE = "22"

exercise_text = input("tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response= requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

Date = today_date
Time = now_time
Exercise = result['exercises'][0]['name']
Duration = result['exercises'][0]['duration_min']
Calories =result['exercises'][0]['nf_calories']


Sheety_endpoint = "https://api.sheety.co/f51e2654cc76e2d347079005a23a6dfe/myWorkouts/workouts"

parameters = {
    "workout": {
        "date": Date,
        "time": Time,
        "exercise": Exercise,
        "duration": Duration,
        "calories": Calories
    }
}

response_sheety = requests.post(Sheety_endpoint, json=parameters, auth=basic)
print(response_sheety.json())