goods=[]
cat=[]
i=0
for i in range(5):
    goods.append(input('请录入商品'))
for item in goods:
    print(item)

search = input('请输入购买的商品')
while True:
    if search=='q':
        print('-'*50)
        print('你的购物车商品为:')
        for item in cat:
            print(item)
        break
    else:
        if search in goods:
            cat.append(search)
            print('商品已经加入购物车')
        else:
            print('商品不存在')
    search = input('请输入购买的商品')
