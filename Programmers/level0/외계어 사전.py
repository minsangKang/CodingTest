from itertools import permutations

def solution(spell, dic):
    for case in permutations(spell, len(spell)):
        if "".join(case) in dic:
            return 1
    return 2