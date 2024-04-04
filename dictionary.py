#Dictionary: key-value pairs, Unsorted, Mutable

mydict = {"name":"Max", "age":28, "city":"new York"}
print(mydict)


mydict2 = dict(name="Mary", age = 23, city="new york")
print(mydict2)

value = mydict['name']
print(value)

mydict['email'] = "max@xyz.com"
print(mydict)

del mydict['name']
print(mydict)

mydict.pop('age')
print(mydict)

#to check the key present or not

if "name" in mydict2:
    print(mydict2["name"])

try:
    print(mydict2["lastname"])
except:
    print("Error")

#to iterate in the dict

for key in mydict2:
    print(key)

for key in mydict2.keys():
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)


# to copy
mydict_cpy = mydict2

#but in this way if we try to modify the copy dict the original also gets modified

# so same as dict use copy() or dict()

mydict_cpyfunc = mydict2.copy()
mydict_dictfunc = dict(mydict2)








