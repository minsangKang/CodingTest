def solution(cards1, cards2, goal):
    i, j = 0, 0
    for target in goal:
        if i < len(cards1) and cards1[i] == target:
            i += 1
        elif j < len(cards2) and cards2[j] == target:
            j += 1
        else:
            return "No"
    return "Yes"