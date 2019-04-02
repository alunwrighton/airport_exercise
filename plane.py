from aircraft import Aircraft

class Plane(Aircraft):
    def __init__(self,name, size, seats, wifi, cinema, flight_attendants):
        self.name= name
        self.size = size
        self.seats = seats
        self.wifi = wifi
        self.cinema = cinema
        self.flight_attendants = flight_attendants

plane1 = Plane("British Airways", "Large", 250,True, True, True)
plane2 = Plane("Turkish Airlines", "Small", 50, False, False, True)
plane3= Plane("Ryan Airways", "Medium", 100, False, True, True)

plane_list = [plane1, plane2, plane3]



