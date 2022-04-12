# 2개 이하로 다른 비트
def solution(numbers):
    answer = []
    for x in numbers:
        x = int(x)
        arr = list('0'+bin(x)[2:])
        index = ''.join(arr).rfind('0')
        arr[index] = '1'
        if x % 2 != 0:
            arr[index+1] = '0'
        answer.append(int(''.join(arr), 2))
    return answer

# Test Case
ret = solution([2,7])
print(ret)