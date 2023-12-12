def solution(survey, choices):
    dict = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    for answer, choice in zip(survey, choices):
        if answer not in dict:
            answer = answer[::-1]
            dict[answer] += 4-choice
        else:
            dict[answer] += choice-4
    
    result = ""
    for key in dict.keys():
        result += key[1] if dict[key] > 0 else key[0]
    return result