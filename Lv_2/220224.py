# 124 나라의 숫자
def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]

# Test Case
ret = solution(1)
print(ret)
ret = solution(2)
print(ret)
ret = solution(3)
print(ret)
ret = solution(4)
print(ret)