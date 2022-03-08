# 다음 큰 숫자
def solution(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m

# Test Case
ret = solution(78)
print(ret)
ret = solution(15)
print(ret)