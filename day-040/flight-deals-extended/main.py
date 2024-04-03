from datetime import datetime
from dotenv import dotenv_values

from flight_data import FlightData
from user_data import UserData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

config = dotenv_values("../../.env")

flight_search = FlightSearch(config['KIWI_KEY'])
flight_data_manager = DataManager(
    'https://www.googleapis.com/auth/spreadsheets',
    "1C4F69eS8bYSZXWvnC3-taxEDpx6ePrBQNVKC4qrOw4Q",
    "prices", '../../google_api_cred.json')
user_data_manager = DataManager(
    'https://www.googleapis.com/auth/spreadsheets',
    "1C4F69eS8bYSZXWvnC3-taxEDpx6ePrBQNVKC4qrOw4Q",
    "users", '../../google_api_cred.json')
mailer = NotificationManager(config["ABV_SMTP"], config["ABV_USER"],
                             config["ABV_PASS"])


def get_flight_data():
    flight_sheet_data = flight_data_manager.get()
    return [FlightData(i + 1, entry[0], entry[1], entry[2]) for i, entry in
            enumerate(flight_sheet_data["values"][1:])]


def get_user_data():
    user_sheet_data = user_data_manager.get()
    return [UserData(i + 1, entry[0], entry[1], entry[2]) for i, entry in
            enumerate(user_sheet_data["values"][1:])]


def validate_flight_data():
    flight_data = get_flight_data()
    for entry in flight_data:
        if len(entry.destination_iata) == 0:
            entry.destination_iata = flight_search.search_iata_code(
                entry.destination_city)
            flight_data_manager.put_at_index(
                entry.id, entry.destination_city, entry.destination_iata,
                str(entry.price))


def search_for_flight_deals():
    flight_data = get_flight_data()
    result = []
    for entry in flight_data:
        search = flight_search.search_flight_deal(entry, entry.stop_overs)
        search_data = None
        if "data" in search and len(search["data"]) > 0:
            search_data = search["data"][0]
        else:
            entry.stop_overs = 10
            search = flight_search.search_flight_deal(entry)
            if "data" in search and len(search["data"]) > 0:
                search_data = search["data"][0]
                entry.via_cities = [f"{r["cityFrom"]}-{r["cityTo"]}" for r in
                                    search_data["route"]]

        if search_data is not None:
            print(f"\n{vars(entry)}")
            print(search_data)
            price = search_data["price"]
            route = search_data["route"]
            departure_city = entry.origin_city
            departure_airport_iata = entry.origin_iata
            arrival_city = entry.destination_city
            arrival_airport_iata = entry.destination_iata
            outbound_date = datetime.fromtimestamp(route[0]["dTime"])
            inbound_date = datetime.fromtimestamp(route[-1]["dTime"])
            output = \
                (f"Price: {price}. "
                 f"Flight {departure_city}-{departure_airport_iata} to "
                 f"{arrival_city}-{arrival_airport_iata}. "
                 f"From {outbound_date} to {inbound_date}")
            if len(entry.via_cities) > 1:
                output += f"\nRoute: {entry.via_cities}"

            print(output)
            if float(price) <= float(entry.price):
                result.append(output)

    return result


def notify_all_users_for_deals():
    deals = "\n\n".join(search_for_flight_deals())
    if len(deals) > 0:
        users = get_user_data()
        for user in users:
            notify_user_for_deals(user.email, deals)


def notify_user_for_deals(email, deals=None):
    if deals is None:
        deals = "\n\n".join(search_for_flight_deals())
    if len(deals) > 0:
        mailer.send(email, "Flight info", deals)


def input_user_data():
    name = input("First name:\n")
    surname = input("Surname:\n")

    email = input("Email address:\n")
    email_validation = input("Validate email address:\n")
    while len(email) == 0 or email != email_validation:
        print("Invalid email, please re-enter.")
        email = input("Email address:\n")
        email_validation = input("Validate email address:\n")

    user_data_manager.append(name, surname, email)


# validate_flight_data()
# input_user_data()
# print(f"\nDEALS: {"\n\n".join(search_for_flight_deals())}")

notify_all_users_for_deals()
