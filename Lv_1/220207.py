# 다트게임
def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1

    return sum(score)

# Test Case
ret = solution('1S2D*3T')
print(ret)
ret = solution('1D2S#10S')
print(ret)
ret = solution('1D2S0T')
print(ret)
ret = solution('1S*2T*3S')
print(ret)
ret = solution('1D#2S*3S')
print(ret)
ret = solution('1T2D3D#')
print(ret)
ret = solution('1D2S3T*')
print(ret)