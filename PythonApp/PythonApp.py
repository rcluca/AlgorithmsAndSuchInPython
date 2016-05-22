from Projects.FlightEmailRetrieval import *

flights = Flight().get_flights();

for flight in flights:
    print flight.departingCities, flight.destinationCities, flight.date, flight.price
