from abc import ABC



class User(ABC):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password



class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def createAccount(self, website):
        website.create_account(self.name, self.email)

class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def createAccount(self, website):
        website.create_account(self.name, self.email)




class website:
    def __init__(self):
        self.cart = []
        self.products = {}
        self.customers_info =[]
        self.sellers_info = []

    def create_account(self, name, email):
        customer = {name, email}
        if()
        self.customers_info.append(customer)

    def place_order(self):
        pass

    def view_products(self):
        pass

    def publish_products(self):
        pass

