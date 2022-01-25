# 정수 제곱근 판별
import math
def solution(n):
    answer = 0
    x = math.sqrt(n)
    if x % 1 == 0:
        answer = (x+1)**2
    else:
        answer = -1
    return answer

# Test Case
ret = solution(121)
print(ret)
ret = solution(3)
print(ret)