# 정수 내림차순으로 배치하기
def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    answer = int("".join(ls))
    return answer

# Test Case
ret = solution(118371)
print(ret)