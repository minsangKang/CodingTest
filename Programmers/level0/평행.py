from itertools import permutations

def solution(dots):
    for case in permutations(dots, 4):
        x1, y1 = case[0]
        x2, y2 = case[1]
        x3, y3 = case[2]
        x4, y4 = case[3]
        angle1 = (y2-y1)/(x2-x1)
        angle2 = (y4-y3)/(x4-x3)
        if angle1 == angle2:
            return 1
    return 0