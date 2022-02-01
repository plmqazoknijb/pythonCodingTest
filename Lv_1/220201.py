# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n],x))

# Test Case
ret = solution(["sun", "bed", "car"],1)
print(ret)
ret = solution(["abce", "abcd", "cdx"],2)
print(ret)