# p와 y의 개수
def solution(s):
    return s.lower().count("p") == s.lower().count("y")

#Test Case
ret = solution("ppPyyY")
print(ret)

ret = solution("pPyyY")
print(ret)

ret= solution("dhfskfef")
print(ret)