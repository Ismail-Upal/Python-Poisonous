class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.product = []

    def __repr__(self) -> str:
        return f'this shop is {self.name}'
    
    def add_product(self, name, price):
        product = Product(name, price)
        self.product.append(product)

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name
    

shop1 = Shop("test shop")
print(shop1.name)
print(shop1)

shop1.add_product("Iphone", 500000)
shop1.add_product("mac", 10000)

shop2 = Shop("test shop 2")
shop2.add_product("monitor", 200000)
shop2.add_product("keyboard", 40000)

print(shop1.product)
print(shop2.product)