# 올바른 괄호
def solution(s):
    answer = True
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

#  Test Case
ret = solution("()()")
print(ret)
ret = solution("(())()")
print(ret)
ret = solution(")()(")
print(ret)
ret = solution("(()(")
print(ret)