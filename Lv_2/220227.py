# 전화번호 목록
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# Test Case
ret = solution(["119", "97674223", "1195524421"])
print(ret)
ret = solution(["123","456","789"])
print(ret)
ret = solution(["12","123","1235","567","88"])
print(ret)