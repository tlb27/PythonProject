def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))

# 解包实参列表
            # 附带两个参数的正常调用
print(list(range(3, 6)))
arr = [3, 6]
print(list(range(*arr)))            # 附带从一个列表解包的参数的调用


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)