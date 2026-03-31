s=0
i=0
while i<=100:
    if i%2==1:
        i += 1
        continue
    s=s+i
    i+=1
print('1-100之间的偶数和是：',s)


sum=0
index=0
for index in range(1,101):
    if index%2==1:
        continue
    sum=sum+index
print('1-100之间的偶数和是：',sum)
