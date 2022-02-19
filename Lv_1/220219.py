# 체육복
def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

# Test Case
ret = solution(5,[2, 4],[1, 3, 5])
print(ret)
ret = solution(5,[2, 4],[3])
print(ret)
ret = solution(3,[3],[1])
print(ret)