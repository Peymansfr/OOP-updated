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



carriage1 = Carriage(1, 10)

carriage1.reserve(1)
carriage1.reserve(2)
carriage1.reserve(7)
carriage1.remove(1)
carriage1.report()

