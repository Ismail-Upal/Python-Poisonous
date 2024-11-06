# static attribute (class attribute)
# static attribute @staticmethon
# class method @classmethod
# difference between static and class method

class Shopping :
    cart = [] # class attribute / static attribute : it will be same for every instance
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = name # instance attribute
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying : {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multipy( a, b):
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu kinmu na just ac er hawa khaite aschi', item)


basundara = Shopping('basu en dhara', 'not popular location')
# basundara.purchase('lungi', 500, 1000)
basundara.hudai_dekhi('lungi')
# Shopping.purchase( 3, 4, 5)  
Shopping.hudai_dekhi('lungi')


Shopping.multipy(3,6) # static method
# basundara.multipy(5,3)


#-------------------------------------------------------------------------
# Python program to demonstrate
# use of class method and static method.
# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)

#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18


# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)

# print(person1.age)
# print(person2.age)

# # print the result
# print(Person.isAdult(22))
#----------------------------------------------------------------------------