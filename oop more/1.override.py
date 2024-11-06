class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        super().__init__(name, age, height, weight)
        self.team = team

    # override :Method overriding, on the other hand, refers to defining a method in a subclass 
    # with the same name as the one in its superclass. The subclass method then overrides the superclass method.
    def eat(self):
        print('vegetable')

    def exercise(self):
        print('gym e poisa dia hudai gham horai')

    # + sign overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign overload
    def __mul__(self, other):
        return self.weight * other.age
    
    # len overload
    def __len__(self):
        return self.height
    
    # > operator overload
    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer('sakib', 38, 68, 91, 'BD')
mushi = Cricketer('mushi', 25, 56, 52, 'BD')
sakib.eat()
sakib.exercise()


#Operator overloading in Python allows you to define how operators like
#  +, -, *, ==, and others behave for your custom objects. This is done by
#  defining special methods, also known as "magic methods" or "dunder methods" 
# (because they start and end with double underscores, e.g., __add__, __eq__).
# + sign Overload
print(45 + 53)
print('sakib' + 'rakib')
print([12, 94] + [2,4,5,6,7])

print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)