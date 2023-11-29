def solution(s):
    x = s[0]
    xCount = 1
    notX = 0
    divisionCount = 1
    for i in range(1, len(s)):
        if xCount == 0 and notX == 0:
            divisionCount += 1
            x = s[i]
        if s[i] == x:
            xCount += 1
        else:
            notX += 1
        if xCount == notX:
            xCount = 0
            notX = 0
    
    return divisionCount