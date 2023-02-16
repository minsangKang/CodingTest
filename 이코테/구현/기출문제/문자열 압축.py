# 압축 문자열 중 가장 짧은 길이 반환
def solution(s):
    minLength = len(s)
    for width in range(1, len(s)//2+1):
        string = ""
        compare = s[0:width]
        count = 1
        index = width
        
        for index in range(width, len(s), width):
            current = s[index:index+width]
            if current == compare:
                count += 1
            else:
                if count > 1:
                    string += str(count)
                string += compare
                compare = current
                count = 1
        
        if count > 1:
            string += str(count)
        
        string += compare
        minLength = min(minLength, len(string))
            
    return minLength