lst = [42,567,324,134,7,23]
print('原数组',lst)

#排序默认升序
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst2=['apple','aAple','banana','Cat','Orange']
print('原数组',lst2)
lst2.sort() #先排大写再排小写
print(lst2)
lst2.sort(reverse=True)
print(lst2)

# 忽略大小写比较
lst2.sort(key=str.lower)
print(lst2)