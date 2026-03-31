lst=['hello','1234',12343]
print(lst)

lst2=list('helloworld')
print(lst2)
lst3=list(range(1,10,2))
print(lst3)

print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst3))
print(lst2.count('l'))
print(lst2.index('l'))


lst4=[10,20,30]
print(lst4)
del lst4[0]
print(lst4)