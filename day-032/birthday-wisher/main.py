import random
import pandas
import datetime as dt

from mailer.gmail import Gmail

birthday_records = pandas.read_csv("birthdays.csv").to_dict(orient="records")
templates = ["letter_templates/letter_1.txt",
             "letter_templates/letter_2.txt",
             "letter_templates/letter_3.txt"]

today = dt.datetime.today()

for record in birthday_records:
    month = int(record["month"])
    day = int(record["day"])
    if day == today.day and month == today.month:
        print(f"{month}-{day}")
        template = random.choice(templates)
        with open(template, "r") as text_file:
            text = text_file.read()
            text = text.replace("[NAME]", record["name"])
            mailer = Gmail("mailer/credentials.json")
            mailer.send_mail(record["email"], "Happy Birthday!", text)
