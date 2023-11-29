from itertools import combinations
# A가 n/2개의 주사위를 고르는 조합 [x]
# n/2개 주사위의 경우에 따른 sum값
# sum 경우의 수에 따른 승, 무, 패 계산
# 승 - 패 값의 max 반영,  선택한 n/2개의 주사위쌍 저장
# return n/2개의 주사위 오름차순

def solution(dice):
    n = len(dice)//2
    maxValue = 0
    maxCaces = []

    dict = {}
    # n/2개의 주사위 선택 (조합)
    for dices in combinations(list(range(n*2)), n):
        dices = list(dices)
        # sum 모든경우 계산
        # 5개 주사위인 경우 -> 1번 index, 2번 index, 3번 index, 4번 index, 5번 index 조합으로 하나의 sum이 계산됌

        if n == 1:
            dict[tuple(dices)] = dice[dices[0]]
        
        elif n == 2:
            dict[tuple(dices)] = calculateFor2Choice(dice, dices, n)

        elif n == 3:
            dict[tuple(dices)] = calculateFor3Choice(dice, dices, n)

        elif n == 4:
            dict[tuple(dices)] = calculateFor4Choice(dice, dices, n)

        elif n == 5:
            dict[tuple(dices)] = calculateFor5Choice(dice, dices, n)
            
    # 각 sums를 기준으로 win, lose 계산
    for key in dict.keys():
        aSums = dict[key]
        bDices = set(list(range(n*2))) - set(list(key))
        bDices = tuple(sorted(list(bDices)))
        bSums = dict[bDices]

        aWin, aLose = calculate(aSums, bSums)
        # 승 - 패 max값 반영
        if (aWin - aLose) > maxValue:
            maxValue = (aWin - aLose)
            maxCaces = list(key)

    return list(map(lambda x: x+1, maxCaces))

def calculate(aSums, bSums):
    aWin, aLose = 0, 0
    for a in aSums:
        for b in bSums:
            if a > b:
                aWin += 1
            elif a < b:
                aLose += 1
    return (aWin, aLose)

def calculateFor2Choice(dice, dices, n):
    sums = []
    # 2가지 주사위의 각 index
    for i in range(6):
        for j in range(6):
            sums.append(dice[dices[0]][i] + dice[dices[1]][j])
    
    return sums

def calculateFor3Choice(dice, dices, n):
    sums = []
    # 3가지 주사위의 각 index
    for i in range(6):
        for j in range(6):
            for k in range(6):
                sums.append(dice[dices[0]][i] + dice[dices[1][j]] + dice[dices[2]][k])
    return sums

def calculateFor4Choice(dice, dices, n):
    sums = []
    # 4가지 주사위의 각 index
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in  range(6):
                    sums.append(dice[dices[0]][i] + dice[dices[1][j]] + dice[dices[2]][k] + dice[dices[3]][l])
    return sums

def calculateFor5Choice(dice, dices, n):
    sums = []
    # 5가지 주사위의 각 index
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        sums.append(dice[dices[0]][i] + dice[dices[1][j]] + dice[dices[2]][k] + dice[dices[3]][l] + dice[dices[4]][m])
    return sums

# 시간초과 개선 목표: A가 승리할 확률 계산 - 모든 경우의 수를 고려해야 하므로 시간초과
# A가 승리하도록 높은 숫자조합의 쌍으로 경우의수를 계산하는 식으로 고려
# 5가지 주사위면 5가지 주사위의 조합 경우만 고려해야 함

print(solution([[103, 100, 100, 100, 100, 100], [102, 100, 100, 100, 100, 100], [101, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100]]))