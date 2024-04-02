class FlightData:

    def __init__(self, id_: int, city: str, iata_code: str, price: float,
                 departure_city: str = "London", departure_iata: str = "LON",
                 currency: str = "GBP"):
        self.id = id_
        self.city = city
        self.iata_code = iata_code
        self.price = price
        self.departure_city = departure_city
        self.departure_iata = departure_iata
        self.currency = currency
