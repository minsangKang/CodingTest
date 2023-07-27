def solution(myString, pat):
    for index, char in list(enumerate(myString)):
        if char == 'A':
            myString[index] = 'B'
        else:
            myString[index] = 'A'
    return 1 if pat in myString else 0
            
print(solution("ABBAA", "AABB"))