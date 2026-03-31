d={10:'12',20:'234',30:'fw',20:'345678'}
print(d)

lst1=[1,3,4,5,6]
lst2=['hello','world','cat']
zip_lst=zip(lst1,lst2)
print(zip_lst)
# print(list(zip_lst))
d=dict(zip_lst)
print(d)

d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t: 10})

# lst=[12,3,5,6]
# print({lst: 10})

print(max(d))
print(min(d))
print(len(d))

del d
# print(d)