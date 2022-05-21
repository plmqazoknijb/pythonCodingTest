# 거스름 돈
def solution(n, money):
    answer = [1] + [0] * n

    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                answer[price] += answer[price - coin]
    return answer[n] % 1000000007

# Test Case
ret = solution(5,[1,2,5])
print(ret)