name='马冬梅'
age=18
score=98.5
print('姓名:%s,年龄:%d,成绩:%f'%(name,age,score))
print('姓名:%s,年龄:%d,成绩:%.1f'%(name,age,score))
print(f'姓名:{name},年龄:{age},成绩:{score}')
print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))

s='helloworld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

print(s.center(20,'*'))
#千分为只适用于整数和浮点数
print('{0:,}'.format(132455432))
print('{0:,}'.format(13245.5432))
# 浮点数精确小数位
print('{0:.1f}'.format(13245.5432))
print('{0:.5}'.format('helloworld'))

a=435
print('二进制{0:b},十进制{0:d},八进制{0:o},十六进制{0:X}'.format(a))

