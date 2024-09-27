# Write what is meant by operator overloading and method overriding with examples.
# ans-> override :Method overriding, on the other hand, refers to defining a method in a subclass 
    # with the same name as the one in its superclass. The subclass method then overrides the superclass method.

#Operator overloading in Python allows you to define how operators like
#  +, -, *, ==, and others behave for your custom objects. This is done by
#  defining special methods, also known as "magic methods" or "dunder methods" 
# (because they start and end with double underscores, e.g., __add__, __eq__).
# + sign Overload
#_________________________________________________________________________
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer('sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('jack', 38, 68, 91)
kalam = Cricketer('kalam', 37, 68,  95)

older = [sakib, musfiq, kamal, kamal, jack, kalam]
old = sakib

for item in older:
    if item > old:
        old = item

print(f'the oldest cricketer is {old.name} with age {old.age}')
#___________________________________________________________________________________
#Write down 4 differences between the class method and static method with proper examples.
#ans->
# classmethod : 
# Definition: A class method takes the class itself as its first argument, typically named cls.
# Usage: It can access and modify class state that applies across all instances of the class. It's often used for factory methods or when you want to modify class variables.
# Declaration: Use the @classmethod decorator.

class MyClass:
    class_variable = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

# staticmethod: 
# Definition: A static method does not take an implicit first argument (neither self nor cls).
# Usage: It behaves like a regular function but belongs to the class's namespace. It's used when the method doesn't need access to the instance or class and is logically related to the class.
# Declaration: Use the @staticmethod decorator.
# python

class MyClass:
    @staticmethod
    def utility_method(x, y):
        return x + y
# Summary
# Use classmethod when you need to work with class-level data.
# Use staticmethod when you don't need access to the class or instance and just want a utility function.
#_____________________________________________________________________________________
#Write what are getter and setter with proper examples
# Getters and setters are methods that provide controlled access to an object's attributes:

# Getters (also called accessors) allow you to retrieve an attribute's value.
# Setters (also called mutators) allow you to modify an attribute's value, often with some validation logic.
# Why Use Getters and Setters?
# Encapsulation: One of the core principles of object-oriented programming (OOP) is encapsulation,
#  which restricts direct access to some of an object's components. By using getters and setters,
#  you can control how attributes are accessed and modified.
# Validation: Setters can enforce rules about the values being assigned to attributes.
#  For example, you can ensure that a person's age is always a non-negative integer.
# Read-Only Attributes: You can define getters without setters to create read-only attributes. 
# This prevents users from modifying the attribute directly while still allowing them to read its value.
# Future-Proofing: If you later decide to change the internal implementation of a class, 
# using getters and setters can help ensure that external code remains unaffected. For example,
#  if you want to compute a value dynamically instead of storing it, you can modify the getter without changing the interface.
#__________________________________________________________________________________________________________________
#Explain the difference between inheritance and composition with proper examples.
# Inheritance: ->
# Definition: Inheritance is a mechanism where a new class (child or subclass) derives properties and behaviors (methods) from an existing class (parent or superclass). This establishes an "is-a" relationship.
# Promotes code reuse by allowing subclasses to inherit attributes and methods from a parent class.
# Can lead to a hierarchical class structure.
# Supports polymorphism, where a subclass can be treated as an instance of its parent class.
# Composition: ->
# Definition: Composition is a design principle where a class is composed of one or more objects from other classes, establishing a "has-a" relationship. Instead of inheriting behavior from a parent class, a class can contain instances of other classes to use their functionality.
# Promotes flexibility and modularity.
# Allows for dynamic changes; you can change the composed objects at runtime.
# Reduces the tight coupling often seen in inheritance.
# Conclusion: ->
# Inheritance is best used when there is a clear hierarchical relationship between classes, allowing for shared behavior and attributes.
# Composition is preferred when you want to create complex types by combining simple ones, promoting flexibility and reducing dependencies between classes.
