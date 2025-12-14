
class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date,stops=0):
        """
        Constructor for initializing a new flight data instance with specific travel details.

        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data):
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries, including the number of stops.

    Args:
        data (dict): The JSON data containing flight information returned by the API.

    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'N/A' if no valid flight data is available.
    """

    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data.get('data'):
        print("No flight data available.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", stops=0)

    # Start with the first flight as the initial cheapest
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    stops = len(first_flight["itineraries"][0]["segments"]) - 1

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)

    # Check all flights in the data
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            stops = len(flight["itineraries"][0]["segments"]) - 1
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)
            print(f"Lowest price to {destination} is £{lowest_price} ({stops} stop(s))")

    return cheapest_flight
