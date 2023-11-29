def solution(k, m, score):
    score = sorted(score, reverse=True)
    result = 0
    for i in range(0, len(score), m):
        if i+m<=len(score):
            box = score[i:i+m]
            result += min(box)*m
    
    return result