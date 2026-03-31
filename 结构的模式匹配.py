data=eval(input('请输入你的数字'))
match data:
    case {'name':'ysj','age':20}:
        print('字典')
    case [10,30,40]:
        print('列表')
    case (19,30,53):
        print('元组')
    case _:
        print('相当于多重if中的else')