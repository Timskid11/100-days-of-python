import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
VIRTUAL_TWILIO_NUMBER = "+1279"
VERIFIED_NUMBER = "+h"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import os

# News API
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Stock API
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

# Twilio
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]


    three_articles_list = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    print(three_articles_list)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for News in three_articles_list:

        message = client.messages.create(
         body=News,
         from_=VIRTUAL_TWILIO_NUMBER,
         to=VERIFIED_NUMBER,
        )

        print(message.status)
