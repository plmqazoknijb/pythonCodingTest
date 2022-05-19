# 멀리 뛰기
def solution(n):
    if n<3:
        return n
    d=[0]*(n+1)
    d[1]=1
    d[2]=2
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]%1234567

# Test Case
ret = solution(4)
print(ret)
ret = solution(3)
print(ret)