import smtplib
import datetime as dt
import random
import os

from dotenv import load_dotenv

load_dotenv()

FRIDAY = 4

now = dt.datetime.now()

if now.weekday() == FRIDAY:
    try:
        with open("quotes.txt") as file:
            quotes = file.readlines()
    except FileNotFoundError:
        print("file not available")
    else:
        daily_quote = random.choice(quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("PW"))
            connection.sendmail(
                from_addr=os.getenv("EMAIL_ADDRESS"),
                to_addrs="stevedearth@icloud.com",
                msg=f"Subject: Friday Inspiration\n\n{daily_quote}")
