# 시저암호
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
    return "".join(s)

# Test Case
ret = solution("AB",1)
print(ret)
ret = solution("z",1)
print(ret)
ret = solution("aBz",4)
print(ret)