# def full_name(first, last):
#     name=f'{first} {last}'
#     return name

# name =full_name('alu', 'kodu')
# print(name)

# name=full_name(last='kodu', first='alu')
# print(name)


def famous_name(first, last, **addition):
    name=f' {first} {last}'
    for key, value in addition.items():
        print(key, value)
    return name

name=famous_name(first='taher', last='ali', title='hujur', addition='sheikh')
print(name)

def a_lot(num1, num2):
    sum=num1+num2
    mul=num1*num2
    rem=num1-num2
    return sum, mul, rem

print(a_lot(43,43))