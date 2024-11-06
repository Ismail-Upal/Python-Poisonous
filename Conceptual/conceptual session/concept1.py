# num =10 #int
# num2=23.4#float
# num3 = 5j#complex
# str = 'C'
# str2="abccd"

# for i in str2:
#     print(i, end=" ")# a b c c d
# print( )
# for i in str2:
#     print(f"this character is {i} and it's type {type(i)}")
# print( )
# for i in range(len(str2)):
#     print(i, end=" ")

# print( )
# for i in range(len(str2)):
#     print(str2[i], end=" ")
# print( )
# for i, val in enumerate(str2):
#     print(f"index: {i} val: {val}")

# a=5
# b=3
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


# i=0
# while(i<5):
#     print(i, end=" ")
#     i+=1

# n = input("enter a number : ")# everythin is string
# n = int(n)

# if n<0:
#     print("negative")
# else :
#     print("positive")

# txt = input()
# if 'a' in txt:
#     print("a is present")
# else:
#     print("a is not present")



def func(a,b):
    return a+b

result = func(3,2)
print(result)

def func(a,b):
    return [a,b]
result = func(2,3)
print(result)

def func(name, *args):
    print(name)
    print(args)
result= func("mahmud" ,3,5,5,2)
result2=func("sakib", 2,5)
print(result)
print(result2)


# from functions import *
# res = func("sakib", 3, 4)
# print(res)

# from folder.functions import *
# res = func("sakib", 3, 4)
# print(res)

amount =100
def func(name, *args):
    global amount
    amount = 500
    print(amount)
func("namer")
print(amount)


numbers = [1,2,3,4,5]
print(numbers[0])
print(numbers[-3])
print(numbers[1 : 3])
print(numbers[0 : 5 : 2])

num = []
for i in range(1,11):
    num.append(i)
print(num)


for i in range(3):
    for j in range(3):
        num.append([i,j])

print(num)