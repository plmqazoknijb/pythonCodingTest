# 제일 작은 수 제거하기
def solution(arr):
    i = min(arr)
    arr.remove(i)
    if len(arr) == 0:
        return [-1]
    return arr

# Test Case
ret = solution([4,3,2,1])
print(ret)
ret = solution([10])
print(ret)