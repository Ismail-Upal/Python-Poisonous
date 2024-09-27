class Vehicle: #grandparent
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def speed(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, capacity) -> None:
        super().__init__(brand, model)
        self.capacity = capacity

class Bike(Vehicle):
    def __init__(self, brand, model, milage) -> None:
        super().__init__(brand, model)
        self.milage = milage

class ElectricCar(Car):
    def __init__(self, brand, model, capacity, battery_capacity) -> None:
        super().__init__(brand, model, capacity)
        self.battery_capacity = battery_capacity


toyota = Car("Toyota", "Corolla", '4')
print(toyota.brand)
print(toyota.capacity)

tesla = ElectricCar("Tesla", "x88", 7, 1000)
print(tesla.brand)
print(tesla.capacity)
print(tesla.battery_capacity)