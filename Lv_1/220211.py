# 폰켓몬
def solution(nums):
    choose = int(len(nums) / 2)  # 주어지는 리스트는 항상 짝수
    nums = set(nums)  # set으로 중복 제거

    answer = min(len(nums), choose)

    return answer

# Test Case
ret = solution([3,1,2,3])
print(ret)
ret = solution([3,3,3,2,2,4])
print(ret)
ret = solution([3,3,3,2,2,2])
print(ret)