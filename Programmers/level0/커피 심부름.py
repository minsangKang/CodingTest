# 카페 라떼: 5000, 아메리카노: 4500
def solution(order):
    result = 0
    for coffee in order:
        if 'cafelatte' in coffee:
            result += 5000
        else:
            result += 4500
    return result