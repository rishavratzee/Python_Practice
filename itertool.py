# itertools: product, permutations, combinations, accumulate, groupby, and ifinite iterators

from itertools import product, permutations, combinations, accumulate, groupby

# product
a=[1,2]
b=[3]

prod = product(a,b, repeat=2)
print(list(prod))

#permutations

a=[1,2,3]
perm = permutations(a)
print(list(perm))

#combinations

a=[1,2,3,4]
comb = combinations(a,2)
print(list(comb))


#accumulate (Compounding sum)
a=[1,2,3,4]
acc = accumulate(a)
print(list(acc))

#multiply
import operator
a=[1,2,3,4]
acc = accumulate(a, func=operator.mul)
print(list(acc))

a=[1,2,3,4]
acc = accumulate(a, func=max)
print(list(acc))

#groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))


