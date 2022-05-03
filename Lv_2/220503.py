# 튜플
def solution(s):
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    result = []
    for l in ls:
        for s in l:
            if int(s) not in result:
                result.append(int(s))
                break
    return result

# Test Case
ret = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
print(ret)
ret = solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
print(ret)
ret = solution("{{20,111},{111}}")
print(ret)
ret= solution("{{123}}")
print(ret)
ret = solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
print(ret)