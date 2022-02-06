# 비밀지도
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # tmp결과 ex) '0b1101'
        tmp = tmp[2:].zfill(n)
        # tmp결과 ex) '01101'
        tmp = tmp.replace('1', '#').replace('0', ' ')
        # tmp결과 ex) ' ## #'
        answer.append(tmp)

    return answer

# Test Case
ret = solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
print(ret)
ret= solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])
print(ret)