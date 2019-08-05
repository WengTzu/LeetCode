import collections

d1 = dict()
d2 = collections.defaultdict(list)
print(d2['a'])
#print(d1['a'])

"""s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = collections.defaultdict(list)
print(d)
for k, v in s:
    print(k, v)
    d[k].append(v)
print(d)
print(list(d.items()))"""