x=10
y=20
num=eval(input('请输入你的中奖号码'))
if num==y:
    print('你中奖了')
else:
    print('你没中奖')
x=10
y=20
max_num=int(0)
if x<y:max_num=y
print(max_num)
grad=eval(input('请输入你的中奖号码'))
result= '你中奖了' if grad == 10 else '你没中奖'
print(result)


if grad == 10:
    print('你中奖了')
elif 0< grad < 20:
    print('很接近了')
elif 40> grad >= 20:
    print('在努努力')
else:
    print('你没中奖')


goods=input('请你说一下吃了什么')
if goods=='apple':
     color=input('什么颜色的')
     if(color=='orange'):
         print('那不是苹果')
     elif(color=='yellow'):
         print('也不是苹果')
     elif(color=='red'):
         print('是苹果')
     else:
         print('你吃错了')
else:
    print('你吃的不对')


iphone=input('请输入你的手机号')
password=input('请输入你的密码')
if iphone and password:
    if len(iphone)==11 and len(password)>8:
        print('可以登录')

    else:
        print('不呢登录')
else:
    print('不能登录')

score=eval(input('请输入成绩'))
if score<0 or score>100:
    print('成绩不正常')