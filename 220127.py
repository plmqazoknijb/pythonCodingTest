# 문자열 다루기 기본
def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

# Test Case
ret = solution("a123")
print(ret)
ret = solution("1234")
print(ret)