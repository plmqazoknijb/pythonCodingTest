# 하샤드 수
def solution(x):
    arr = list(str(x))
    sum_x = 0
    for i in arr:
        sum_x += int(i)
    return x % sum_x == 0

# Test Case
ret = solution(10)
print(ret)
ret = solution(11)
print(ret)
ret = solution(12)
print(ret)
ret = solution(13)
print(ret)