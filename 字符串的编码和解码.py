s='伟大的中国梦'
c=s.encode(errors='replace')
# 编码
print(c)
b=s.encode('gbk',errors='replace')
print(b)

s2='✌️耶'
print(s2.encode('gbk',errors='strict'))
