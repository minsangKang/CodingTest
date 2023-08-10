def solution(name, yearning, photo):
    result = []
    for p in photo:
        result.append(sum([yearning[name.index(n)] for n in p if n in name]))
    return result