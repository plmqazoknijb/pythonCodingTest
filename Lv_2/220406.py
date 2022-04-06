# 삼각 달팽이
import itertools

def snailNext(x,y,d_snail) :
    if d_snail %3 ==0 :
        x+=1
    elif d_snail %3 ==1 :
        y+=1
    else :
        x-=1
        y -=1
    return x,y

def solution(n):
    tri_snail = [[0 for k in range(1,i+1)] for i in range(1,n+1) ]
    direct_snail = range(n)
    x, y= -1, 0
    idx = 1
    for d_snail in direct_snail :
        for i in range(d_snail, n) :
            x,y = snailNext(x,y,d_snail)
            tri_snail[x][y]= idx
            idx+=1
    return list(itertools.chain(*tri_snail))

# TestCase
ret = solution(4)
print(ret)
ret = solution(5)
print(ret)
ret = solution(6)
print(ret)