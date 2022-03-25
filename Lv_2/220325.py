# 점프와 순간 이동
def solution(n):
    cnt = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1
    return cnt

# Test Case
ret = solution(5)
print(ret)
ret = solution(6)
print(ret)
ret = solution(5000)
print(ret)