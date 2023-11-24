def solution(name, yearning, photo):
    result = []
    for p in photo:
        score = 0
        for n in p:
            if n in name:
                score += yearning[name.index(n)]
        result.append(score)
    return result