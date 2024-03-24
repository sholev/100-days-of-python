import datetime as dt

import random

from mailer import Mailer


class Main:

    def __init__(self):
        with open("quotes.txt", "r") as quotes:
            self.quotes = quotes.readlines()

    def get_random_quite(self):
        random_quote = random.choice(self.quotes)
        return random_quote

    def send_quote(self):
        weekday = dt.datetime.now().strftime('%A')
        mailer = Mailer("", "", "")
        mailer.send("", f"{weekday}'s quote", self.get_random_quite())


main = Main()
main.send_quote()
