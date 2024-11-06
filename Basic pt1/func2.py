def all_sum (num1, num2, *numbers):
    print(numbers)
    sum=0
    for n in numbers:
        print(n)
        sum+=n
    return sum

total = all_sum(43, 434, 53, 43, 3434)
print('total sum : ', total)


