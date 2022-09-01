import itertools

def startAndGetCount(order, dungeons, k):
    energe = k
    count = 0
    for index in order:
        if dungeons[index][0] <= energe:
            energe -= dungeons[index][1]
            count += 1
        else:
            break
    return count

def solution(k, dungeons):
    maxCount = 0
    indexs = list(range(0,len(dungeons)))

    npr = itertools.permutations(indexs, len(dungeons))
    for order in npr:
        maxCount = max(maxCount, startAndGetCount(order, dungeons, k))
    
    return maxCount

answer = solution(80, [[80,20],[50,40],[30,10]])
print(answer)