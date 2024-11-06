def call():
    print('calling someone')
    return 'call done'

class Phone:
    price = 3245
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending sms to: {phone} and messege: {sms}'
        return text


my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(1234, 'missy, i missed to miss you')
print(result)
