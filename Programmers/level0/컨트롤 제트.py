def solution(s):
    chars = s.split()
    result = []
    for index, char in enumerate(chars):
        if char == 'Z':
            result.pop()
        else:
            result.append(int(char))
    return sum(result)