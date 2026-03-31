 #sdbs
for i in 'hello world':
    print(i)

for j in range(3,10):
    if j % 2 == 0:
        print(j)

num=0
for i in range(1,10):
    num+=i
else:
    print('else',num)


for i in range(100,1000):
    sd=i%10
    ten=i//10%10
    bai=i//100
    if sd**3+ten**3+bai**3==i:
        print('水仙花数',i)