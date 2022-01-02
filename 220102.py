# 최대공약수와 최소공배수
from math import gcd
def solution(n, m):
    gcd_ = gcd(n,m)
    lcm = n*m // gcd(n,m)
    return gcd_,lcm

#TestCase
ret = solution(3,12)
print(ret)

ret = solution(2,5)
print(ret)