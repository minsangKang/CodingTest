# 문자열 w가 올바른 괄호 문자열인지 확인하는 함수
def isRight(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return True if len(stack) == 0 else False            

# 균형잡힌 문자열 u 분리하는 함수
def divide(w):
    count = 0
    u = []
    for i in w:
        u.append(i)
        if i == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            break
    return ("".join(w[:len(u)]), "".join(w[len(u):]))

# 문자열 뒤집기
def flip(u):
    result = ""
    for i in u:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result
    
# 올바른 괄호 문자열로 변환한 결과를 반환
def rightString(p):
    if p == "":
        return ""
    u, v = divide(p)
    if isRight(u):
        v = rightString(v)
        return u + v
    else:
        result = "("
        result += rightString(v)
        result += ")"
        result += flip(u[1:-1])
        return result

# 올바른 괄호 문자열로 변환한 결과를 반환
def solution(p):
    return rightString(p)
        