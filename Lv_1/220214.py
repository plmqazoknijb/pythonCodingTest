# 신고 결과 받기
def solution(id_list, report, k):
    db = {name:[] for i, name in enumerate(id_list)}
    reports = {name:0 for i, name in enumerate(id_list)}

    for re in set(report):
        user = re.split(" ")[0]
        reported_user = re.split(" ")[1]
        db[user].append(reported_user)
        reports[reported_user] +=1

    answer = [0 for _ in range(len(id_list))]
    for key, values in db.items():
        for value in values:
            if reports[value] >=k:
                answer[id_list.index(key)] += 1
    return answer

# Test Case
ret = solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
print(ret)
ret = solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)
print(ret)