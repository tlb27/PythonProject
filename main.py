# coding=utf-8
# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
a=2
b=3
print(chr(76))
print(oct(23))
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {a*b}')  # 按 ⌘F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
fp=open('test.txt','w')
fp.write('Hello World')
fp.close()

# name= input('Enter your name: ')
# print("我的名字是:"+ name)

num=input('请输入一个你的幸运数字: ')
print('你的幸运数字是：'+num)
num=int(num)
print('你的幸运数字是：',num)

'''
print(chr(76))
print(oct(23))
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age