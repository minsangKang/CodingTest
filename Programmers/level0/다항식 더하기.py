def solution(polynomial):
    hangs = polynomial.split(" + ")
    xNum = 0
    num = 0
    for hang in hangs:
        if 'x' in hang:
            xNum += 1 if hang == 'x' else int(hang[:-1])
        else:
            num += int(hang)
    
    if xNum == 0:
        return str(num)

    result = "x" if xNum == 1 else str(xNum)+'x'
    if num == 0:
        return result
    return result + " + " + str(num)