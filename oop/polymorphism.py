# poly = many (many)
# morph = different (shape)

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('gheo gheo')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meh meh')

shepard = Dog('local shepard')
shepard.make_sound()

don = Cat('real don')
don.make_sound()

messi = Goat('L M')
messi.make_sound()

lessi = Goat('gora gori')
animals = [don, shepard, messi, lessi]
for animal in animals:
    animal.make_sound()