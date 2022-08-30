def type(dict, leftKey, rightKey):
    return leftKey if dict[leftKey] == max(dict[leftKey], dict[rightKey]) else rightKey

def solution(survey, choices):
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        score = choices[i] - 4
        if score < 0:
            dict[survey[i][0]] += (-score)
        elif score > 0:
            dict[survey[i][1]] += score
    type1 = type(dict, "R", "T")
    type2 = type(dict, "C", "F")
    type3 = type(dict, "J", "M")
    type4 = type(dict, "A", "N")
    answer = type1+type2+type3+type4
    return answer

answer = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
print(answer)