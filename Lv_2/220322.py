# 쿼드압축 후 개수 세기
def solution(arr):
    h = len(arr) // 2
    if sum([sum(i) for i in arr]) == len(arr)*len(arr[0]):
        return [0, 1]
    elif sum([sum(i) for i in arr]) == 0:
        return [1, 0]
    else:
        return [sum(i) for i in zip(*[solution([i[:h] for i in arr[:h]]),
                                      solution([i[h:] for i in arr[:h]]),
                                      solution([i[:h] for i in arr[h:]]),
                                      solution([i[h:] for i in arr[h:]])])]

# Test Case
ret = solution ([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
print(ret)
ret = solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
print(ret)