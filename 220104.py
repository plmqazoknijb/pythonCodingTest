#평균 구하기
def solution(arr):
    arr_sum = 0
    avg = len(arr)
    for i in arr:
        arr_sum += i
    answer = arr_sum / avg
    return answer

#Test Case
ret = solution([1,2,3,4])
print(ret)

ret = solution([5,5])
print((ret))