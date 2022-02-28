# 최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer

# Test Case
ret = solution([1,4,2],[5,4,4])
print(ret)
ret = solution([1,2],[3,4])
print(ret)