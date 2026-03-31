d={'hello':10,'world':20,'python':30}
print(d.items())
print(list(d.items()))
print(dict(d.items()))
print(d.keys())
print(tuple(list(d.keys())))
print(d.values())

s=d.pop('hello','sdfgh')
print(s)
print(d)

c=d.popitem()
print(c)
print(d)

d.clear()
print(d)
print(bool(d))