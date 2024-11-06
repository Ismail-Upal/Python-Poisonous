class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name} (Price: {self.price} tk)'


class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def __repr__(self) -> str:
        return f'Shop: {self.name}'
    
    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)
        print(f'Product {name} added to {self.name}')

    def buy_product(self, name, customer_money):
        for product in self.products:
            if product.name == name:
                if customer_money >= product.price:
                    print(f'Congrats! You have bought {product.name} for {product.price} tk.')
                    if customer_money > product.price:
                        change = customer_money - product.price
                        print(f'Here is your change: {change} tk.')
                    return
                else:
                    print(f'Not enough money to buy {product.name}. You need {product.price - customer_money} tk more.')
                    return
        print(f'Sorry, {name} is not available in {self.name}.')


# Example usage:
shop1 = Shop("Local Store")
shop1.add_product("Chips", 10)
shop1.add_product("Juice", 30)

# Buying products
shop1.buy_product("Chips", 15)  # Successful purchase with change
shop1.buy_product("Juice", 25)  # Not enough money
shop1.buy_product("Soda", 20)   # Product not available

# what is inheritance with exmples
# what are the encaptulation and access modifier?