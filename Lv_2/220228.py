# 최댓값과 최솟값
def solution(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))

# Test Case
ret = solution("1 2 3 4")
print(ret)
ret = solution("-1 -2 -3 -4")
print(ret)
ret = solution("-1 -1")
print(ret)