try:
    i = int(input('请输入成绩'))
    if 0<=i<=100:
        print('你的分数为',i)
    else:
        raise Exception('分数不正确')
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
