# 행렬의 덧셈
def solution(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

# Test Case
ret = solution([[1,2],[2,3]],[[3,4],[5,6]])
print(ret)

ret = solution([[1],[2]],[[3],[4]])
print(ret)