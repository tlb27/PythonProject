



try:
    a = int(input('请输入一个数'))
    b = int(input('请输入一个数'))
    result = a/b
    print(result)
except ZeroDivisionError:
    print('除数为零')
except ValueError:
    print('不能输入字母')
except BaseException:
    print('未知异常')