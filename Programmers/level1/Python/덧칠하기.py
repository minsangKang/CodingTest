def solution(n, m, section):
    result = 1
    startNum = section[0]
    for num in section:
        endNum = startNum+m-1
        if startNum <= num and num <= endNum:
            continue
        else:
            result += 1
            startNum = num
    return result