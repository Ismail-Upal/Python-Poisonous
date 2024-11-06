# set : unique items collection
# set --> {}
# tuple --> ()
# list --> []
numbers= [12,32,45,52,43,43, 23]
numbers=set(numbers)
print(numbers)

numbers.add(33)
print(numbers)

numbers.remove(12)
print(numbers)

for item in numbers:
    print(item)

if 9 in numbers:
    print('exist')
else:
    print('not ')
    
#numbers[1]=34 immutable

A={1,3,5}
B={1,2,3,4,5}
print(A&B)
print(A|B)
