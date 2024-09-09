numbers=[34,45,65,64,63,34, 64, 43, 53, 72,44]
odd=[]
for num in numbers:
    if num%2==1 and num%5==0:
        odd.append(num)
print(odd)


odd_nums= [num for num in numbers if num%2==1 if num%5==0]
print(odd_nums)


players= ['sakib', 'musfik', 'mustafiz']
ages=[23,53,53]
age_comb=[]
for player in players:
    print('player: ', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])
print(age_comb)


age_comb2= [[player, age] for player in players for age in ages]
print(age_comb2)