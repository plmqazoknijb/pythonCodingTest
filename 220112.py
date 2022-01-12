# 음양 더하기
def solution(absolutes,signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# Test Case
ret = solution([4,7,12],[True,False,True])
print(ret)
ret = solution([1,2,3],[False,False,True])
print(ret)