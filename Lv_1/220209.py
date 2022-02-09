# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# Test Case
ret = solution([1,2,3,4,6,7,8,0])
print(ret)
ret = solution([5,8,4,0,6,7,9])
print(ret)