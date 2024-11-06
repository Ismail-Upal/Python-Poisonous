class Shop:
    shopping_mall = 'jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute\

    def add_to_cart(self, item):
        self.cart.append(item)


mehzabeen = Shop('meh zab een')
mehzabeen.add_to_cart('shoe')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = Shop('nishi night er nisho')
nisho.add_to_cart('hat')
nisho.add_to_cart('watch')
print(nisho.cart)

apurvo = Shop('purbho chilo')
apurvo.add_to_cart('chironi')
print(apurvo.cart)