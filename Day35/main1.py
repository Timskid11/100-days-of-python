import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
load_dotenv()

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

import os

# Twilio
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

# OpenWeatherMap
OWM_Endpoint = os.getenv('OWM_Endpoint')
API_KEY = os.getenv('API_KEY')

parameter = {
    "appid" : API_KEY,
    "lat" :   6.457060,
    "lon" : 3.212420 ,
    "cnt" : 4,
    "units" : "metric",
             }
will_rain = False
response = requests.get(OWM_Endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) < 700:
    will_rain = True
if will_rain:
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!☔☂️",
        from_="+13612",
        to="+2348104",
    )

    print(message.status)