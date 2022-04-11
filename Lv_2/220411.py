# 이진 변환 반복하기
def solution(s):
    answer = []

    cnt = 0
    zero = 0

    while True:
        if s == '1':
            break
        zero = zero + s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:]

        cnt = cnt + 1

    answer = [cnt, zero]

    return answer

# Test Case
ret = solution("110010101001")
print(ret)
ret = solution("01110")
print(ret)
ret = solution("1111111")
print(ret)