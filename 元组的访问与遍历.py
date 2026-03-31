t=('hello','world','goodbye')
print(t[0])
print(t[0:3:2])

for i in t:
    print(i)

for i in range(len(t)):
    print(i,t[i])

for index,item in enumerate(t):
    print(index,item)

for index,item in enumerate(t,11):
    print(index,item)