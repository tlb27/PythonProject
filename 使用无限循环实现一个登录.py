


s=0
i=1
while i<11:
    s=s+i
    if s>20:
        print('推出循环',i)
        break
    i+=1



i=0
while i<3:
    userName=input('用户名')
    password=input('密码')
    if userName=='tlb' and password=='123':
        print('登录中')
        break
    else:
        if i<2:
            print('你还有',2-i,'次机会')
            i+=1
        else:
            print('请你稍厚在试')
            break

