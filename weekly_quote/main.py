import smtplib
import datetime as dt
import random

My_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(My_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL, msg=f"Subject: Monday Motivation\n\n")
