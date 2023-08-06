def solution(bin1, bin2):
    # 1. bin(이진수, 2) 함수와 bin 함수 사용
    return bin(int(bin1, 2)+int(bin2, 2))[2:]

    # 2. 직접 구현
    bin1 = "0"*(10-len(bin1))+bin1
    bin2 = "0"*(10-len(bin2))+bin2
    result = [0]*11
    
    for i in range(10):
        if bin1[i] == '1':
            result[i+1] += 1
        if bin2[i] == '1':
            result[i+1] += 1
    
    for i in range(10, 0, -1):
        if result[i] > 1:
            result[i] -= 2
            result[i-1] += 1
    
    resultString = "".join(map(str, result))
    return resultString[resultString.find('1'):]