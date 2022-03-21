# n^2배열 자르기
def solution(n, left, right):
    result = []
    for i in range(int(left), int(right + 1)):
        result.append(max(i // n, i % n) + 1)
    return result

# Test Case
ret = solution(3,2,5)
print(ret)
ret = solution(4,7,14)
print(ret)