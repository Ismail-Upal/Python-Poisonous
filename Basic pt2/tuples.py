things = 'pen', 'tripod', 'bottle', 'phone'
print(things)
print(things[0])
print(things[-2])
print(things[1:3])

if 'phone' in things:
    print ('exist')

for item in things:
    print(item)

# things[0]='wagon' immutabel or not assignable

print(len(things))

mega=([3,3,5], [2,6,3])
print(type(mega))

mega[0][1]=343 #list inside tuple is mutable
print(mega)