class Phone:
    manufactured = 'china'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def __init__(self, phone, sms):
        text = f'sending to {phone} {sms}'
        print(text)