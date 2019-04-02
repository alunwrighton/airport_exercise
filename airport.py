# Creating Airport class

class Airport:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.terminals = []

# Creating Terminal class

class Terminal:

    def __init__(self, name, location, airport):
        self.name = name
        self.location = location
        self.airport = airport
        self.flights = []

    def add_flights(self, flight):
        self.flights.append(flight)

heathrow = Airport("Heathrow", "London")

terminal1 = Terminal("T1", "North", heathrow)
terminal1.add_flights("FG145")
print(terminal1.flights)

