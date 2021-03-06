# 전력망을 둘로 나누기
from collections import deque


def bfs(start, visitied, graph):
    queue = deque([start])
    result = 1
    visitied[start] = True
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                queue.append(i)
                visitied[i] = True

    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, not_visit in wires:
        visitied = [False] * (n + 1)
        visitied[not_visit] = True
        result = bfs(start, visitied, graph)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))

    return answer

# Test Case
ret = solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
print(ret)
ret = solution(4,[[1,2],[2,3],[3,4]])
print(ret)
ret = solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])
print(ret)