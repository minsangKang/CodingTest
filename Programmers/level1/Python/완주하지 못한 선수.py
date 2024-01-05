def solution(participant, completion):
    dict = {}
    for name in participant:
        if name not in dict:
            dict[name] = 1
        else:
            dict[name] += 1
    
    for name in completion:
        dict[name] -= 1
        if dict[name] == 0:
            del dict[name]
            
    return list(dict.keys())[0]