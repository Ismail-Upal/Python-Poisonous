class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'

    def move(self):
        pass


class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class pickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACbus(Bus):
    def __init__(self, name, price, seat, temp) -> None:
        self.temp = temp
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()


green_line = ACbus('green', 50000, 22, 13)
print(green_line)