from datetime import datetime
from dotenv import dotenv_values

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

config = dotenv_values("../../.env")

flight_search = FlightSearch(config['KIWI_KEY'])
data_manager = DataManager('https://www.googleapis.com/auth/spreadsheets',
                           "1C4F69eS8bYSZXWvnC3-taxEDpx6ePrBQNVKC4qrOw4Q",
                           "prices", '../../google_api_cred.json', )
mailer = NotificationManager(config["ABV_SMTP"], config["ABV_USER"],
                             config["ABV_PASS"])

data = data_manager.get_flight_data()
for entry in data[1:]:
    if len(entry.iata_code) == 0:
        entry.iata_code = flight_search.search_iata_code(entry.city)
        data_manager.put_at_index(entry.id, entry)

    print(vars(entry))
    search = flight_search.search_flight_deal(entry, 1)

    if "data" in search and len(search["data"]) > 0:
        search_data = search["data"][0]
        print(search_data)
        outbound_route = search_data["route"][0]
        inbound_route = search_data["route"][-1]
        price = search_data["price"]
        departure_city = outbound_route["cityFrom"]
        departure_airport_iata = outbound_route["flyFrom"]
        arrival_city = outbound_route["cityTo"]
        arrival_airport_iata = outbound_route["flyTo"]
        outbound_date = datetime.fromtimestamp(outbound_route["dTime"])
        inbound_date = datetime.fromtimestamp(inbound_route["dTime"])
        output = (f"Price: {price}. "
                  f"Flight {departure_city}-{departure_airport_iata} to "
                  f"{arrival_city}-{arrival_airport_iata}. "
                  f"From {outbound_date} to {inbound_date}")
        print(output)
        if float(price) <= float(entry.price):
            mailer.send(config["GMAIL_USER"], "Flight info", output)

