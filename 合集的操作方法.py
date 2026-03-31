a={12,4,6,72}
a.add(10)
print(a)
a.remove(12)
print(a)
# a.clear()
# print(a)

# 遍历集合
for item in a:
    print(item)


for index,item in enumerate(a):
    print(index,item)

s={i for i in range(10,20)}
print(s)


s={i for i in range(10,20) if i%2==0}
print(s)