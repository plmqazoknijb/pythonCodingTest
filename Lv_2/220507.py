# 메뉴 리뉴얼
from itertools import combinations

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        new_menu = {}
        for menu in orders:
            menu_li = list(''.join(menu))
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                if res not in candidates:
                    candidates.append(res)
                else:
                    if res not in new_menu.keys():
                        new_menu[res] = 2
                    else:
                        new_menu[res] += 1
        sort_menu = sorted(new_menu.items(), key=lambda x:[len(x[0]), x[1]])
        if len(sort_menu):
            now = course[-1]
            maxi = sort_menu[-1][1]
        while sort_menu:
            menu, cnt = sort_menu.pop()
            if len(menu) == now and cnt >= maxi:
                answer.append(menu)
            elif len(menu) != now:
                now = len(menu)
                maxi = cnt
                answer.append(menu)
    return sorted(answer)

# Test Case
ret = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
print(ret)
ret = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])
print(ret)
ret = solution(["XYZ", "XWY", "WXA"],[2,3,4])
print(ret)