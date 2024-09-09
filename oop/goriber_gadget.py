# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand, price,origin,  color) -> None:
        self.brand = brand
        self.price = price
        self.origin = origin
        self.color = color

    def run(self):
        return f'running laptop: {self.brand}'



class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    def coding(self):
        return f'learning python and practise'
    
class Phone(Gadget):
    def __init__(self,brand, price, color,  origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'sending SMS to : {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass



# inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
print(my_phone)
print(my_phone.brand)