from itertools import combinations

def solution(number):
    count = 0
    for case in combinations(number, 3):
        if sum(case) == 0:
            count += 1
    
    return count