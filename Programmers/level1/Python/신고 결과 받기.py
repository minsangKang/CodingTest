# 2차원배열 대신 dict, 두번 for문 확인 방법
def solution(id_list, report, k):
    nameToIndex = {name: idx for idx, name in enumerate(id_list)}
    reports = {name : 0 for name in id_list}

    # 사람별 신고 count 저장
    for r in set(report):
        reports[r.split()[1]] += 1
    # 신고개수에 따라 신고사람 메일수신 count 증가
    answer = [0]*len(id_list)
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[nameToIndex[r.split()[0]]] += 1

    return answer


# 신고 한 사람들을 배열로 지닌 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {id: [] for id in id_list}
    for r in set(report):
        r = r.split()
        reports[r[1]].append(r[0])
    # 신고한 사람들 각각 +1로 계산
    for id, reporters in reports.items():
        if len(reporters) >= k:
            for id in reporters:
                answer[id_list.index(id)] += 1

    return answer


# 더러운 나의 풀이
def solution(id_list, report, k):
    nameToIndex = {name: idx for idx, name in enumerate(id_list)}
    relation = [[0]*len(id_list) for _ in range(len(id_list))]
    # a가 b를 신고
    for names in report:
        a, b = names.split()
        relation[nameToIndex[a]][nameToIndex[b]] = 1
    # 사람별 정지여부
    terminated = [False]*len(id_list)
    # b 고정, a 순차
    for b in range(len(id_list)):
        sum = 0
        for a in range(len(id_list)):
            sum += relation[a][b]
        # b 의 신고횟수 저장
        if sum >= k:
            terminated[b] = True
    # 각 신고대상 확인
    result = []
    for a in range(len(relation)):
        count = 0
        for b in range(len(relation)):
            if relation[a][b] == 1 and terminated[b] == True:
                count += 1
        result.append(count)
        
    return result
