class Pen:
    made_in = 'Bangladesh'
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price


my_pen=Pen('black', 'matador', 6)
print(my_pen.brand, my_pen.color, my_pen.price)
her_pen=Pen('blue', 'gdluck', 5)
print(her_pen.brand, her_pen.color, her_pen.price)
his_pen=Pen('red', 'eco', 10)
print(his_pen.brand, his_pen.color, his_pen.price)
