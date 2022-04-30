# 타겟 넘버
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

# Test Case
ret = solution([1, 1, 1, 1, 1],3)
print(ret)
ret = solution([4, 1, 2, 1],4)
print(ret)