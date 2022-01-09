# 나누어 떨어지는 숫자 배열
def solution(arr,divisor):
    answer=[]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
    return answer

# Test Case
ret = solution([5, 9, 7, 10],5)
print(ret)
ret = solution([2, 36, 1, 3],1)
print(ret)
ret = solution([3,2,6],10)
print(ret)