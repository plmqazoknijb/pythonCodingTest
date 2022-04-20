# 문자열 압축
def solution(s):
    answer = 10000
    for n in range(1, len(s) // 2 + 2):
        res = ''
        cnt = 1
        tmp = s[:n]

        for i in range(n, len(s) + n, n):
            if tmp == s[i:i + n]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[i:i + n]
                cnt = 1
        answer = min(answer, len(res))
    return answer

# Test Case
ret = solution("aabbaccc")
print(ret)
ret = solution("ababcdcdababcdcd")
print(ret)
ret = solution("abcabcdede")
print(ret)
ret = solution("abcabcabcabcdededededede")
print(ret)
ret = solution("xababcdcdababcdcd")
print(ret)