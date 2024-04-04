#lists: Ordered, mutable, allows duplicate elements

myList = ["apple","banana","orange"]
print(myList)

mylist2 = list()
print(mylist2)

for fruit in myList:
    print(fruit)

if "orange" in myList:
    print("yes")
else:
    print("No")


print(len(myList))

myList.append("lemon")
print(myList)

myList.insert(1,"blueberry")
print(myList)

item = myList.remove("lemon")
print(item)

print(myList)

item = myList.pop()
print(item)

myList.reverse()

myList.sort()

#if you do not want to change original list
myListSorted = sorted(mylist2)

# myList.clear()


#new list with 5 zero
mylisrZero = [0] * 5

mylist2 = [1] * 5

myListAdded = mylist2 + mylisrZero
print(myListAdded)

#slicing

myList3 = [1,2,3,4,5,6,7,8,9]

a = myList3[1:5]
print(a)



list_org = ["apple","banana","orange"]

list_cpy = list_org

#in order to copy not keep reference to original list use copy()
list_cpy2 = list_org.copy()

#or use
list_cpy3 = list(list_org)

list_cpy.append("lemon")
list_cpy2.append("not ment to be appende in original")

print(list_cpy)
print(list_org)
print(list_cpy2)

#in order to copy not keep reference to original list use copy()
list_cpy2 = list_org.copy()

#fast way to create a list from existing list
num = [1,2,3,4,5,6]
num_square = [i*i for i in num]

print(num_square)