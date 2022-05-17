# 하노이의 탑
def solution(n):
    def hanoi(n, From, Toward, Sub):
        if n == 1:
            answer.append([From, Toward])
            return
        hanoi(n - 1, From, Sub, Toward)
        answer.append([From, Toward])
        hanoi(n - 1, Sub, Toward, From)

    answer = []
    hanoi(n, 1, 3, 2)
    return answer

# Test Case
ret = solution(2)
print(ret)