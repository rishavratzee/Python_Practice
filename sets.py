#Sets: Unordered, mutable, no duplicates


myset = {1,2,3}
print(myset)

myset2 = set("Hello")
print(myset2)

myset3 = {}  # this will be considered an empty dictionary and not set
print(type(myset3))

# so create an empty set like this
myset4 = set()
print(type(myset4))

myset.add(4)
print(myset)

myset.remove(1)

myset.discard(1) # this error safe

print(myset.pop())


for i in myset:
    print(i)

if 1 in myset:
    print("Yes")
else:
    print("no")



odds = {1,3,5,7,9}
even = {0,2,4,6,8}
primes = {2,3,5,7}

#union

u = odds.union(even)
print(u)


#intersection

intr = primes.intersection(even)
print(intr)


#diff

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

#subset
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3}
print(setA.issubset(setB))

print(setA.issuperset(setB))


#copy is same as dict




