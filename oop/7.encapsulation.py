# encapsulation --> hide details
# access modifier : public, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self.__balance = initial_deposit # private attribute (only can be acces from class)
        self._branch = 'banani branch' # protected 

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'fokira tk nai'
        


rafsan = Bank('choto bro', 1000)
# rafsan.holder_name = 'boro vai'
print(rafsan.holder_name)

rafsan.deposit(2423)
# rafsan.balance = 0
print(rafsan.get_balance())
print(rafsan._branch)


print(dir(rafsan))
print(rafsan._Bank__balance)