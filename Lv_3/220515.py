# 야근 지수
import heapq

def solution(works,n):
    answer = 0
    heap=[]

    for work in works:
        heapq.heappush(heap, (-work, work))

    while True:
        if n==0:
            break
        work=heapq.heappop(heap)[1]-1
        heapq.heappush(heap, (-work, work))
        n-=1

    for h in heap:
        if h[1] < 0:
            continue
        answer+=h[1]**2

    return answer

# Test Case
ret = solution([4, 3, 3],4)
print(ret)
ret = solution([2, 1, 2],1)
print(ret)
ret = solution([1,1],3)
print(ret)