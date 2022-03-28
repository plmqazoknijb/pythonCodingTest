# 위장
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1

# Test Case
ret = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
print(ret)
ret = solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
print(ret)