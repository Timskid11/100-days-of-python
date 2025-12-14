import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d6976b386aa19bc72c7168d56d2c65e7/flightDeals/prices"
SHEETY_USERS_ENDPOINT="https://api.sheety.co/d6976b386aa19bc72c7168d56d2c65e7/flightDeals/users"

response = requests.get(url=f"{SHEETY_USERS_ENDPOINT}")
response.raise_for_status()
print(response.json)