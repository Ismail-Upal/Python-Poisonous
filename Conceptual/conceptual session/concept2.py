# a=10
# b=10
# print(id(a))# id for address
# print(id(b))

# # string : immutable
# # tuple (): immutable
# # list []: mutable
# # set {}: unordered, unindexed
# # dictionary dict{}
# c="rahim"
# c=list(c)
# c[0]='f'
# c = "".join(c) # for loop er moto kaj kre
# print(c)


# lst = [1,2,2,2,3,3,3,4,5]
# lst = set(lst)
# lst = list(lst)
# print(lst)

# lst = lst[::-1]
# lst.reverse()
# print(lst)

# a = "madam"
# print(a==a[::-1])

# lst = [1,2,2,2,3,3,3,4,5]
# dic = { item: lst.count(item) for item in lst}
# print(dic)

# lst={1,5,7,3,9,12,6}
# value =5
# for i,j in enumerate(lst):
#     print(i,j)


# new_lst = [i for i,j in enumerate(lst) if j>value]
# print(new_lst)


dic1={'rahim':10, 'karim':20, 'fahim':23}
dic2={'rahim':12, 'karim':43, 'fahim':27}
print(dic1.keys())
print(dic1.values())
print(dic1.items())