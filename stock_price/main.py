from dotenv import load_dotenv
from datetime import date, timedelta
import requests
import os

load_dotenv()

STOCK = "AUDC"
COMPANY_NAME = "Audiocodes"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_FUNCTION = "TIME_SERIES_DAILY"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": STOCK_FUNCTION,
    "symbol": STOCK,
    "apikey": os.getenv("ALPHA_VANTAGE_KEY")
}

news_parameters = {
    "apiKey": os.getenv("NEWS_API_KEY"),
    "qInTitle": COMPANY_NAME,
    "pageSize": 3
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
daily_info = response.json()["Time Series (Daily)"]

#since python 3.6, dictionary is insertion ordered, so this should be
#safe
daily_data = [value for (key, value) in daily_info.items()]
yesterday_close = float(daily_data[0]["4. close"])
previous_day_close = float(daily_data[1]["4. close"])
increase = yesterday_close - previous_day_close
change = abs(increase) / yesterday_close
should_get_news = change > 0.05

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if should_get_news:
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    if data["totalResults"] > 0:
        for article in data["articles"]:
            print(article["title"])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
### can do with the send_sms code in this project instead if I wanted to do it

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

