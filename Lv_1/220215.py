# 숫자 문자열과 영단어
def solution(s):
    answer = 0
    en = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx,num in enumerate(en):
        if num in s:
            s = s.replace(num,str(idx))
        answer = s
    return int(answer)

# Test Case
ret = solution("one4seveneight")
print(ret)
ret = solution("23four5six7")
print(ret)
ret = solution("2three45sixseven")
print(ret)
ret = solution("123")
print(ret)