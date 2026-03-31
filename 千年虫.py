lst=[88,89,90,98,0,99]
# for index in range(len(lst)):
#     if lst[index]==0:
#         lst[index]='200'+str(lst[index])
#     else:
#         lst[index]='19'+str(lst[index])
#
# print(lst)


for index,value in enumerate(lst):
    if value==0:
        lst[index]='200'+str(value)
    else:
        lst[index]='19'+str(value)

print(lst)