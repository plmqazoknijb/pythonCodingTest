# 자연수 뒤집어 배열로 만들기
def solution(n):
    ls = list(str(n))
    ls.reverse()
    answer = list(map(int,ls))
    return answer

# Test Case
ret = solution(12345)
print(ret)