#lambda arguments : expression

add10 = lambda x : x + 10
print(add10(5))

#similar to 

def add10_func(x):
    return x+10


mult = lambda x,y : x*y
print(mult(2,7))


point2D = [(1,2), (15,1), (5,-1), (10,4)]
point2D_sorted = sorted(point2D, key= lambda x : x[1]) # to sort it based on the y index
print(point2D)
print(point2D_sorted)

#similar to

def sort_by_y(x):
    return x[1]

#sort it based on the sum of the coordinates
point2D = [(1,2), (15,1), (5,-1), (10,4)]
point2D_sorted = sorted(point2D, key= lambda x : x[0]+x[1]) # to sort it based on the y index
print(point2D)
print(point2D_sorted)

#map(func, seq/list)

a = [1,2,3,4,5]
b = map(lambda x : x*2, a)
print(list(b))

#filter(func, seq)
a = [1,2,3,4,5,6]
b = filter(lambda x : x%2==0, a)
print(list(b))

#reduce(func, seq)
from functools import reduce
a = [1,2,3,4,5,6]
prod_a = reduce(lambda x,y : x*y, a)
print(prod_a)


