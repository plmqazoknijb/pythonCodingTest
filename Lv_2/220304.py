# JadenCase 문자열 만들기
def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer

# Test Case
ret = solution("3people unFollowed me")
print(ret)
ret = solution("for the last week")
print(ret)