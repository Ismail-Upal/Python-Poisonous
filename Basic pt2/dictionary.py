numbers = {12,56,98,78,56,12,26,98}
person=['kala chan', 'kalipur', 23, 'student']
# key value pair == dictionary == object == hash table== overlap with set

person = {'name':'kala pakhi', 'address':'kaliapur', 'age':23, 'job':'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

person['language']='python'
person['name']= 'sada pakhi'
del person['age']
print(person)

for key, value in person.items():
    print(key, value)