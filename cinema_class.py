class City:
    def __init__(self, name, state, zip_code):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code 

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

class Cinema:
    def __init__(self, name, total_cinema_halls, address: Address, halls):
        self.__name = name
        self.__total_cinema_halls = total_cinema_halls
        self.__location = address
        self.__halls = halls

class CinemaHallSeat:
    def __init__(self, id, seat_type):
        self.__hall_seat_id = id
        self.__seat_type = seat_type

class CinemaHall:
    def __init__(self,hall_id, name, total_seats, seats: CinemaHallSeat, shows):
        self.hall_id=hall_id
        self.name = name
        self.total_seats = total_seats
        self.seats = seats
        self.shows = shows

