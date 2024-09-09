class Shopping:
    def __init__(self, name):
        self.name= name
        self.cart= []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            #print(item) 
            total += item['price']* item['quantity']
        print('total price:  ', total)
        if amount< total:
            print( f'please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'here is your items and extra money {extra}')

    def remove_from_cart(self, item_nam):
        for productt in self.cart:
            if productt['item']==item_nam:
                self.cart.remove(productt)
                break
    

swapan = Shopping('Alan shopon')
swapan.add_to_cart('alu', 24, 3)
swapan.add_to_cart('dim', 12, 23)
swapan.add_to_cart('rice', 46, 34)


print(swapan.cart)
#swapan.checkout(12600)
swapan.checkout(234)
swapan.remove_from_cart('alu')
swapan.checkout(234)