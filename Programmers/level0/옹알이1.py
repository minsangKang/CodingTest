import itertools

def solution(babbling):
    base = ['aya', 'ye', 'woo', 'ma']
    answers = ['aya', 'ye', 'woo', 'ma']
    for i in range(2, 4+1):
        permutations = list(itertools.permutations(base, i))
        for permutation in permutations:
            answers.append("".join(list(permutation)))
            
    count = 0
    for bab in babbling:
        if bab in answers:
            count += 1
            
    return count