# 내적
def solution(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

# Test Case
ret = solution([1,2,3,4],[-3,-1,0,2])
print(ret)
ret = solution([-1,0,1],[1,0,-1])
print(ret)