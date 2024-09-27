# Customer
# Employee
# Admin

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary) -> None:
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee('rahim', 'rahim@gmail.com', 12321, 'Dhaka', 23, 'Chef', 12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.employees = [] # database 

    def add_employee(self, name, email, phone, address):
        