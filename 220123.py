# x만큼 간격이 있는 n개의 숫자
def solution(x,n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

# Test Case
ret = solution(2,5)
print(ret)
ret = solution(4,3)
print(ret)
ret = solution(-4,2)
print(ret)