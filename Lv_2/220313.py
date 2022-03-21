# 주차 요금 계산
import math

def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h * 60 + m

def solution(fees, records):
    answer = []
    dt, df, ut, uf = fees
    dic = dict()
    for r in records:
        time, number, history = r.split()
        number = int(number)
        if number in dic:
            dic[number].append([dateToMinutes(time), history])
        else:
            dic[number] = [[dateToMinutes(time), history]]
    rList = list(dic.items())
    rList.sort(key=lambda x: x[0])
    for r in rList:
        t = 0
        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]
        if r[1][-1][1] == "IN":
            t += dateToMinutes('23:59')
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t - dt) / ut) * uf)
    return answer

# Test Case
ret = solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print(ret)
ret = solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
print(ret)
ret = solution([1, 461, 1, 10],["00:00 1234 IN"])
print(ret)