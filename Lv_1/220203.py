# 2016년
import datetime
def solution(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

# Test Case
ret = solution(5,24)
print((ret))