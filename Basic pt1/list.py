numbers=[23,53,34,43]


for i, num in enumerate(numbers):# with index
    print(i,num)
    


numbers.append(45)
print(numbers)

numbers.insert(3, 34)
print(numbers)

numbers.remove(34)
print(numbers)

if 34 in numbers:
    numbers.remove(34)
print(numbers)

last= numbers.pop()
print(last, numbers)

index = numbers.index(53)
print(index)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)