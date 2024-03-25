import random
import pandas
import datetime as dt

from mailer.gmail import Gmail

templates = ["letter_templates/letter_1.txt",
             "letter_templates/letter_2.txt",
             "letter_templates/letter_3.txt"]

today = dt.datetime.today()
df = pandas.read_csv("birthdays.csv")
today_records = df[(df['month'] == today.month) & (df['day'] == today.day)]
mailer = Gmail("mailer/credentials.json")

for index, row in today_records.iterrows():
    template = random.choice(templates)
    with open(template, "r") as text_file:
        text = text_file.read()
        text = text.replace("[NAME]", row["name"])
        mailer.send_mail(row["email"], "Happy Birthday!", text)
