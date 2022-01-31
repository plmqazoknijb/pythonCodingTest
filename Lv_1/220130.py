# 부족한 금액 계산하기
def solution(price,money,count):
    sum_price = 0
    for i in range(1,count+1):
        cot_price = price * i
        sum_price += cot_price

    if sum_price > money:
        return sum_price - money
    else:
        return 0

# Test Case
ret = solution(3,20,4)
print(ret)
ret = solution(3,20,2)
print(ret)