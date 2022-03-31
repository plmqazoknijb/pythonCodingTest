# 카펫
def solution(brown, yellow):
    s = brown + yellow
    for i in range(s,2,-1):
        if s % i ==0:
            a = s//i
            if yellow == (i-2)*(a-2):
                return [i,a]

# Test Case
ret = solution(10,2)
print(ret)
ret = solution(8,1)
print(ret)
ret = solution(24,24)
print(ret)