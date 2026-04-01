def get_sum(num):
    s=0
    for i in range(1,num+1):
        s=s+i
    # return s
res=get_sum(10)
print(res)


def get_text(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)

get_text(1,2,2,kwd1=1, kwd2=2)