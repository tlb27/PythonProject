import random

d={item:random.randint(1,100) for item in range(4,10)}
print(d)

lst=[1,3,4,56,6]
lst2=['hello','world','cat','dog']
d={key:value for key,value in zip(lst,lst2)}
print(d)
