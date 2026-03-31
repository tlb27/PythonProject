list=['hello','world','python','php']
for item in list:
    print(item)

for i in range(0,len(list)):
    print(i,list[i])


for i,j in enumerate(list):
    print(i,j)


for index,item in enumerate(list,1):
    print(index,item)
