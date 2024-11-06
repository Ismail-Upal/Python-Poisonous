from abc import ABC, abstractmethod

class Shape(ABC):
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
        return 3.1416 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.1416 * self.radius


rect = Rectangle(3,4)
print(rect.area())
print(rect.perimeter())

circle = Circle(5)