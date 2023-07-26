def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i%2 == 0:
                ret += code[i]
            elif code[i] == '1':
                mode = 1
        else:
            if code[i] != '1' and i%2 == 1:
                ret += code[i]
            elif code[i] == '1':
                mode = 0
    return ret if len(ret)>0 else 'EMPTY'