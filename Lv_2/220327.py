# 구명보트
def solution(people, limit):
    people.sort()
    cnt = 0;
    i = 0; j = len(people)-1
    while i <= j:
        cnt += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return cnt

# Test Case
ret = solution([70, 50, 80, 50],100)
print(ret)
ret =solution([70, 80, 50],100)
print(ret)