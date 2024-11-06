class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
        self.__balance = 500

    def __repr__(self) -> str:
        return f"This shop is {self.name}"
    
    def add_product(self, name, price):
        product = Product(name , price)
        self.products.append(product)

    def sell(self):
        self.balance += product.price

    def __tax_added(self):
        return self.__balance * 0.10
    
    def get_balance(self):
        return self.__balance - self.__tax_added()

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name
    

shop1 = Shop("Test shop")
print(shop1)
shop1.add_product("Iphone", 50000)
shop1.add_product("Macbook", 10000)

# print(shop1.balance)
# shop1.balance = 0

print(shop1.get_balance())