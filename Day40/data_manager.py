import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d6976b386aa19bc72c7168d56d2c65e7/flightDeals/prices"
SHEETY_USERS_ENDPOINT="https://api.sheety.co/d6976b386aa19bc72c7168d56d2c65e7/flightDeals/users"


class DataManager:

    def __init__(self):
        self.prices_endpoint = os.getenv("SHEET_PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("SHEET_USERS_ENDPOINT")
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):

        try:
            # Make GET request to the users sheet endpoint with basic auth
            response = requests.get(
                url=self.users_endpoint,

            )

            # Raise an error if the request failed
            response.raise_for_status()

            # Parse JSON response
            data = response.json()

            # Extract emails from the 'users' sheet
            # NOTE: Adjust 'users' key to match your sheet's JSON structure
            emails = [user["email"] for user in data["users"]]

            return emails

        except requests.exceptions.RequestException as e:
            print(f"Error fetching customer emails: {e}")
            return []
