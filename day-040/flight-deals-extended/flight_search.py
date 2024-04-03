import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from flight_data import FlightData


class FlightSearch:

    def __init__(self, key):
        self.url = "https://api.tequila.kiwi.com"
        self.headers = {
            "accept": "application/json",
            "apikey": key,
        }

    def search_iata_code(self, city: str) -> str:
        data = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 10,
            "active_only": True,
            "sort": "",  # For A->Z use 'sort=name', for Z->A use 'sort=-name'
        }
        endpoint = f"{self.url}/locations/query"
        r = requests.get(endpoint, params=data, headers=self.headers)
        json_data = r.json()
        locations = json_data["locations"]
        if len(locations) > 0:
            city = locations[0]["city"]["code"]
            return city

    def search_flight_deal(self, data: FlightData, limit: int = 1):
        date_now = datetime.now()
        tomorrow_date = date_now + timedelta(days=1)
        limit_date = date_now + relativedelta(months=6)
        data = {
            "fly_from": data.origin_iata,
            "fly_to": data.destination_iata,
            "curr": data.currency,
            "date_from": tomorrow_date.strftime("%d/%m/%Y"),
            "date_to": limit_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "sort": "price",
            "max_stopovers": data.stop_overs,
            "limit": limit,
        }
        endpoint = f"{self.url}/search"
        r = requests.get(endpoint, params=data, headers=self.headers)
        json_data = r.json()
        return json_data
