#tuples: ordered, immutable, allows duplicate elements

myTuple = ("Max", 28, "Boston")
print(myTuple)

#we can emmit the paranthesis
myTuple2 = "Max", 28, "Boston"
print(myTuple2)

#for single tuple use comma at the end otherwise it will be considered as a string
myTuple3 = ("Max",)
print(type(myTuple3))

myTuple4 = ("max")
print(type(myTuple4))

#use built in tuple function
myTupleFnc = tuple(["Max",28,"Boston"])
print(myTupleFnc)

item  = myTupleFnc[0];
print(item)

# myTupleFnc[0] = "tim"   # not possible as tuple is immutable

for i in myTupleFnc:
    print(i)


if "Max" in myTupleFnc:
    print("Yes")
else:
    print("No")


myTupleLetters = ('a','b','c','d','e')
print(len(myTupleLetters))

print(myTupleLetters.count('a')) # count of an item in the tuple
print(myTupleLetters.index('a'))  # first occurance of the item


#convert a tuple to a list and vice versa

my_list = list(myTuple)
print(my_list)
list_to_tuple = tuple(my_list)
print(list_to_tuple)


#slicing same as in list


name, age, city = myTuple
print(name)
print(age)
print(city)

my_new_tuple = (0,1,2,3,4,5)

i1, *i2, i3 = my_new_tuple

print(i1)
print(i2)
print(i3)

