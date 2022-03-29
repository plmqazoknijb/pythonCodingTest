# 큰 수 만들기
def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])

# Test Case
ret = solution("1924",2)
print(ret)
ret = solution("1231234",3)
print(ret)
ret = solution("4177252841",4)
print(ret)