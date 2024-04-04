# Collections: Counter, namedtuple, OrderedDict, defaultDict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

#counter
a = "aaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)

print(my_counter.keys())
print(my_counter.values())


# to print the most common keys
print(my_counter.most_common(2))
print(my_counter.most_common(2)[0])
print(my_counter.most_common(2)[0][0])

print(list(my_counter.elements()))

#namedTuple

point = namedtuple('point','x,y') # this will create a class with x and y variables
pt = point(1,-4)
print(pt.x,pt.y)


#OrderedDict

orderd_dict = OrderedDict()
orderd_dict['c'] = 1
orderd_dict['b'] = 2
orderd_dict['a'] = 3
orderd_dict['d'] = 4

print(orderd_dict)

# defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])


#deque

d = deque()

d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()

d.extend([4,5,6])
print(d)

d.extendleft([1,2,3])
print(d)


d.rotate(1)
print(d)



