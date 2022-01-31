# 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    for x in range(1,n):
        if n % x == 1:
            answer = x
            break
    return answer

# Test Case
ret = solution(10)
print(ret)
ret = solution(12)
print(ret)