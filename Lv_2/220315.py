# n진수 게임
def convert(i, n):
    T = "0123456789ABCDEF"
    q, r = divmod(i, n)
    if q == 0:
        return T[r]
    else:
        return convert(q, n) + T[r]

def solution(n, t, m, p):
    result = ""
    i = 0
    while len(result) < m * t:
        result += convert(i, n)
        i += 1
    return result[p-1::m][:t]

# Test Case
ret = solution (2,4,2,1)
print(ret)
ret = solution(16,16,2,1)
print(ret)
ret = solution(16,16,2,2)
print(ret)