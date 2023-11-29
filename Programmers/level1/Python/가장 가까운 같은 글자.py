def solution(s):
    dict = {}
    result = []
    for idx, char in enumerate(s):
        if char in dict:
            result.append(idx - dict[char])
        else:
            result.append(-1)
        dict[char] = idx
    return result
            