# 양궁대회
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0   # 라이언이 이길때 가장큰 점수 차이
    # 1. 중복 조합을 이용해 라이언의 점수를 만든다.
    for res in list(combinations_with_replacement(range(0, 11), n)):
        now = [0 for _ in range(11)]
        for r in res:
            now[10 - r] += 1
        lion = 0
        peach = 0
        # 2. 라이언 점수와 어피치 점수 비교한다.
        for i, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:
                peach += (10 - i)
            elif l > p:
                lion += (10 - i)
        if lion > peach:
            win = True
            if (lion - peach) > max_num:
                max_num = lion - peach
                answer = now
    if not win:
        return [-1]
    return answer

# Test Case
ret = solution(5,[2,1,1,1,0,0,0,0,0,0,0])
print(ret)
ret = solution(1,[1,0,0,0,0,0,0,0,0,0,0])
print(ret)
ret = solution(9,[0,0,1,2,0,1,1,1,1,1,1])
print(ret)
ret = solution(10,[0,0,0,0,0,0,0,0,3,4,3])
print(ret)