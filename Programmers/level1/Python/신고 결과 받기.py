def findTargetIndexs(map, k):
    counts = [0]*len(map[0])
    for row in range(len(map[0])):
        for column in range(len(map[0])):
            counts[column] += map[row][column]
    
    targetIndexs = []
    for idx in range(len(counts)):
        if counts[idx] >= k:
            targetIndexs.append(idx)
    
    return targetIndexs

def findAnswer(map, targetIndexs):
    answers = [0]*len(map[0])

    for column in range(len(map[0])):
        if not(column in targetIndexs):
            continue
        for row in range(len(map[0])):
            answers[row] += map[row][column]

    return answers

def solution(id_list, report, k):
    # map 생성
    map = [[0]*len(id_list) for i in range(len(id_list))]
    # map update
    for rep in report:
        start, to = rep.split()
        startIdx = id_list.index(start)
        toIdx = id_list.index(to)
        map[startIdx][toIdx] = 1
    # k -> filter
    targetIndexs = findTargetIndexs(map, k)
    # map, targetIndexs -> answer
    return findAnswer(map, targetIndexs)