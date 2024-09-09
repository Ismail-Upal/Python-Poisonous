# base class, parent class, common attribute + functionality class
# derived class ,child class, uncommone attribute + functionality class

class Device:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    


class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'running laptop: {self.brand}'
    
    def coding(self):
        return f'learning python and practise'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

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
