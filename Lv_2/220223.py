# N개의 최소공배수
def solution(arr):
    from math import gcd
    answer = arr[0]

    for num in arr:
        answer = answer*num // gcd(answer, num)

    return answer

# Test Case
ret = solution([2,6,8,14])
print(ret)
ret = solution([1,2,3])
print(ret)