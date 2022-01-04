#짝수와 홀수
def solution(num):
    answer = ""
    if num % 2 == 0 or num == 0:
        answer = "Even"
    elif num % 2 == 1:
        answer = "Odd"
    return answer

#Test Case
ret = solution(3)
print(ret)
ret = solution(4)
print(ret)