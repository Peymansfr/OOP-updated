class Carriage:
    def __init__(self, number, seats):
        self.number = number
        self.seats = seats
        self.reserved_seats = set()

    def reserve(self, seat_number):
        if not self.is_full() and seat_number not in self.reserved_seats and seat_number in range(1, self.seats + 1):
            self.reserved_seats.add(seat_number)
            print(f'The seat {seat_number} is reserved')
        else:
            print("No seats available")

    def remove(self, seat_number):
        if seat_number in self.reserved_seats:
            self.reserved_seats.remove(seat_number)
            print(f'The seat {seat_number} is removed')
        else:
            print("No seats to remove")

    def reset(self):
        self.reserved_seats.clear()
        print("The seats are reset")

    def is_full(self):
        return self.seats == len(self.reserved_seats)

    def report(self):
        print(f"Carriage {self.number} has {self.seats - len(self.reserved_seats)} seats available"
              f" and {len(self.reserved_seats)} seats reserved")
        if self.reserved_seats:
            print(f"Reserved seats: {', '.join(str(seat) for seat in self.reserved_seats)}")

class Train:
    def __init__(self, train_id, departure, destination, carriages):
        self.train_id = train_id
        self.departure = departure
        self.destination = destination
        self.carriages = carriages

    def add_carriage(self, carriage, position=None):
        if position is None:
            self.carriages.append(carriage)
        else:
            self.carriages.insert(position, carriage)
        print(
            f"Carriage {carriage.number} is added to the train at position {position if position is not None else 'end'}")

    def remove_carriage(self, carriage_number):
        self.carriages = [carriage for carriage in self.carriages if carriage.number != carriage_number]
        print(f"Carriage {carriage_number} removed from the train")

    def reserve_seat(self, carriage_number, seat_number):
        for carriage in self.carriages:
            if carriage.number == carriage_number:
                carriage.reserve(seat_number)
                return
            print("No such carriage")

    def report(self):
        for i in range(len(self.carriages)):
            print(f"Reserved seats in carriage {i + 1}:")
            self.carriages[i].report()

carriage1 = Carriage(1, 10)
carriage2 = Carriage(2, 15)
train = Train("T123", "Helsinki", "Turku", [carriage1, carriage2])
train.reserve_seat(1, 1)
train.reserve_seat(2, 5)
train.remove_carriage(2)
train.remove_carriage(2)