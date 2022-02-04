# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        now_count = 0;
        for j in range(1, i + 1):
            if i % j == 0:
                now_count += 1;

        if now_count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

# Test Case
ret = solution(13,17)
print(ret)
ret = solution(24,27)
print(ret)