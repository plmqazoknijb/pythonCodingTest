# 피로도
answer = 0


def enter(dungeons, k, i, visited):
    global answer
    visited = visited[:]
    visited[i] = 1
    k -= dungeons[i][1]
    answer = max(answer, sum(visited))

    for j in range(len(dungeons)):
        if not visited[j] and dungeons[j][0] <= k:
            enter(dungeons, k, j, visited)


def solution(k, dungeons):
    visited = [0] * len(dungeons)

    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            enter(dungeons, k, i, visited)

    return answer

# Test Case
ret = solution(80,[[80,20],[50,40],[30,10]])
print(ret)