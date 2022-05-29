# 이중우선순위큐
import heapq

def solution(operations):
    answer = []
    heap = []

    for data in operations:
        if data[0] == "I":
            heapq.heappush(heap, int(data[2:]))
        else:
            if len(heap) == 0:
                pass
            elif data[2] == "-":
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)

    return answer

# Test Case
ret = solution(["I 16","D 1"])
print(ret)
ret = solution(["I 7","I 5","I -5","D -1"])
print(ret)