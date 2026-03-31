# 直接创建集合
d={10,30,4,50}
print(d)
# 集合只能存储不可变数据类型
# s={[12,4],[5,5]}
# print(s)

s=set() #创建一个空集合
print(s,type(s))
s={4,5}
print(s,type(s))

s=set('helloworld')
print(s,type(s))

s2=set([10,20,30])
print(s2,type(s2))

s3=set(range(10))
print(s3,type(s3))

print(max(s3))
print(min(s3))
print(len(s3))
print(5 in s3)
print(10 not in s3)

del s3
print(s3)
