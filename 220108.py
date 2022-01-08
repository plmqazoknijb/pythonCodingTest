# 서울에서 김서방 찾기
def solution(seoul):
    answer = ''
    for index, x in enumerate(seoul):
        if x =='Kim':
            answer = f'김서방은 {index}에 있다'
    return answer

# Test Case
ret = solution(["Jane", "Kim"])
print(ret)