from collections import ChainMap, Counter

# ChainMap holds a list of mappings that can be searched as one
# The lookup is performed on each input mapping in the order
# it appears in the constructor call

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

chain = ChainMap(d1, d2)
chain['a']
chain['c']

assert 6 == chain['c']

# ChainMap holds references to the input mappings
chain['c'] = -1

print((d1, d2))

counter = Counter('abracadabra')
counter.update('aaaaazzz')

assert [('a', 10), ('z', 3), ('b', 2)] == counter.most_common(3)
