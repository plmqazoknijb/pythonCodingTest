# 캐시
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    buffer = deque()
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in cities:
            i = i.lower()
            if i in buffer: answer += 1
            else: answer += 5

            if i in buffer:
                buffer.remove(i)
            else:
                if len(buffer) >= cacheSize:
                    buffer.popleft()

            buffer.append(i)
    return answer

# Test Case
ret = solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
print(ret)
ret = solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
print(ret)
ret = solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
print(ret)
ret = solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
print(ret)
ret = solution(2,["Jeju", "Pangyo", "NewYork", "newyork"])
print(ret)
ret = solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
print(ret)