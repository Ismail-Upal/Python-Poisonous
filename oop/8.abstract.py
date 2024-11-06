from abc import ABC, abstractclassmethod
# abstract base class
class Animal(ABC):
    @abstractclassmethod  # enforce all derive class to have a eat method
                        # must have methods in derived class from parent class
    def eat(self):
        print('I need food')
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('hey i am eating banana')
    def move(self):
        print('hanging on the branches')

layka = Monkey('lucky')
layka.eat()


# abstract vs interface (interview question)