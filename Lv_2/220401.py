# H-Index
def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

# Test Case
ret = solution([3, 0, 6, 1, 5])
print(ret)