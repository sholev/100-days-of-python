class FlightData:

    def __init__(self, id_: int, destioation_city: str, destination_iata: str,
                 price: float, origin_city: str = "London",
                 origin_iata: str = "LON", currency: str = "GBP",
                 stop_overs: int = 0, via_cities: str = None):
        self.id = id_
        self.destination_city = destioation_city
        self.destination_iata = destination_iata
        self.price = price
        self.origin_city = origin_city
        self.origin_iata = origin_iata
        self.currency = currency
        self.stop_overs = stop_overs
        self.via_cities = via_cities
        if self.via_cities is None:
            self.via_cities = [""]
