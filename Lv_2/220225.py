# 가장 큰 수
def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))

# Test Case
ret = solution([6,10,2])
print(ret)
ret = solution([3,30,34,5,9])
print(ret)