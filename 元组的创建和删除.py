# t=('hello',[1,3,5])
# print(t)
text=str(122)
print(text)
t=tuple('hello')
print(t)

t=tuple([13,3,4,513,10])
print(t)

print('10在元组中是否存在',('10' in t))
print(max(t))
print(min(t))
print(sum(t))
print(len(t))
print(t.index(10))
print(t.count(10))
t=(10,)
print(t,type(t))

# del t
# print('删除后',t)