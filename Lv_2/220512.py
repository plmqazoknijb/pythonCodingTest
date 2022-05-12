# 최고의 집합
def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    initial = s//n
    for _ in range(n):
        answer.append(initial)
    idx = len(answer) - 1
    for _ in range( s % n):
        answer[idx] += 1
        idx -= 1
    return answer

# Test Case
ret = solution(2,9)
print(ret)
ret = solution(2,1)
print(ret)
ret = solution(2,8)
print(ret)