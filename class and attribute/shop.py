class Shop:
    cart= [] # cart is class attribute
    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehzabeen = Shop('meh ja been')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nishu = Shop('noisho')
nishu.add_to_cart('cap')
nishu.add_to_cart('watch')
print(nishu.cart)