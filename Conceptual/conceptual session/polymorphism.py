from abc import ABC, abstractmethod
from math import pi
class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return pi * self.radius**2
    
    def perimeter(self):
        return pi * self.radius * 2
    

rect = Rectangle(3,4)
print("rectangle area: ",rect.area())
print("rectangle perimeter: ", rect.perimeter())

circle = Circle(5)
print("circle area: ", circle.area())
print("circle perimeter: ", circle.perimeter())