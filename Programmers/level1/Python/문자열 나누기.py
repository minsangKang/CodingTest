def solution(s):
    result = []
    while s:
        x = s[0]
        xCount, nxCount = 1, 0
        
        for i in range(1, len(s)):
            if s[i] == x:
                xCount += 1
            else:
                nxCount += 1
                
            if xCount == nxCount:
                result.append(s[0:i])
                s = s[i+1:]
                break
                
        if xCount != nxCount:
            result.append(s)
            break
                
    return len(result)