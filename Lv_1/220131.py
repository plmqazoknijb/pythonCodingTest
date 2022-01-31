# 문자열 내림차순으로 배치하기
def solution(s):
    s_list = list(s)
    s_list.sort(reverse= True)
    answer = "".join(s_list)
    return answer

# Test Case
ret = solution("Zbcdefg")
print(ret)