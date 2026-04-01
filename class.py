# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
# x = Complex(3.0, -4.5)
# print(x.r)
# print(x.i)
#
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter

# class Dog:
#
#     kind = 'canine'         # 类变量被所有实例所共享
#
#     def __init__(self, name):
#         self.name = name    # 实例变量为每个实例所独有
#
# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.kind)
# print(e.kind)
# print(d.name)
# print(e.name)
# 
# class Dog:
# 
#     tricks = []             # 类变量的错误用法
# 
#     def __init__(self, name):
#         self.name = name
# 
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# 
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# d.tricks                # 非预期地被所有的 Dog 实例所共享
# # ['roll over', 'play dead']
# print(d.tricks)
#
# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # 为每个 Dog 实例新建一个空列表
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# d.tricks
# # ['roll over']
# print(d.tricks)
# e.tricks
# # ['play dead']
# print(e.tricks)

# class Warehouse:
#    purpose = 'storage'
#    region = 'west'
#
# w1 = Warehouse()
# print(w1.purpose, w1.region)
#
# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)

# 在类之外定义的函数
# class Bag:
#     def __init__(self):
#         self.data = []
#
#     def add(self, x):
#         self.data.append(x)
#
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # 原始 update() 方法的私有副本

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # 为 update() 提供了新的签名
        # 但不会破坏 __init__()
        for item in zip(keys, values):
            self.items_list.append(item)