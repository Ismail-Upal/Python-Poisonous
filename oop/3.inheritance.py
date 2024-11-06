# base class, parent class, common attribute + functionality class
# derived class ,child class, uncommone attribute + functionality class

class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running laptop: {self.brand}'

class Laptop:
    def __init__(self, brand, price, color, memory, ssd) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        self.ssd = ssd

    def run(self):
        return f'running laptop: {self.brand}'
    
    def coding(self):
        return f'learning python and practise'
    
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def run(self):
        return f' phone tipa tipi kore'
    
    def phone_call(self, number, text):
        return f'sending SMS to : {number} with: {text}'
    
class Camera:
    def __init__(self, brand, price , color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass
    
    def change_lens(self):
        pass


my_phone = Phone('iphone', 120000, 'silver', 'china', True)
print(my_phone)

print(my_phone.brand)