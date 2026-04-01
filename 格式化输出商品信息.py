lst=[
    ['01','电风扇','美的',500],
    ['02','电视吉','小米',1500],
    ['03','净水器','海尔',5200],
]
print('编号\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for p in item:
        print(p,end='\t\t')
    print()

for item in lst:
    item[0]='0000'+item[0]
    item[3]='¥{0:.2f}'.format(item[3])

print('编号\t\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for p in item:
        print(p,end='\t\t')
    print()
