# 3진법 뒤집기
def solution(n):
    answer = ''
    while n > 0:
        n,mod = divmod(n,3)
        answer += str(mod)
    return int(answer,3)

# Test Case
ret = solution(45)
print(ret)
ret = solution(125)
print(ret)