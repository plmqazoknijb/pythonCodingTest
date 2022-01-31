# 소수 찾기
def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)

# Test Case
ret = solution(10)
print(ret)
ret = solution(5)
print(ret)