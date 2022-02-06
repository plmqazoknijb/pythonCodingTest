# 최소직사각형
def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)

# Test Case
ret = solution([[60, 50], [30, 70], [60, 30], [80, 40]])
print(ret)
ret = solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
print(ret)
ret = solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
print(ret)
