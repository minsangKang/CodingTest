def solution(s):
    dict = {}
    result = []
    for i in range(len(s)):
        if s[i] in dict:
            result.append(i - dict[s[i]])
        else:
            result.append(-1)
        dict[s[i]] = i
    return result