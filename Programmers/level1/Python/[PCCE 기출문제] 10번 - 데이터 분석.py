# [코드번호, 제조일, 최대수량, 현재수량]
def solution(data, ext, val_ext, sort_by):
    dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    filtered = filter(lambda x: x[dict[ext]] < val_ext, data)
    return sorted(filtered, key=lambda x: x[dict[sort_by]])