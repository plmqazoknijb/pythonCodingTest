# 소수 만들기
from itertools import combinations


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))

    for i in arr:
        sum = i[0] + i[1] + i[2]
        if isPrime(sum):
            answer += 1
    return answer

# Test Case
ret = solution([1,2,3,4])
print(ret)
ret = solution([1,2,7,6,4])
print(ret)