# 예산
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

# Test Case
ret = solution([1,3,2,5,4],9)
print(ret)
ret = solution([2,2,3,3],10)
print(ret)