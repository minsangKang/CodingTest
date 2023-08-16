def solution(k, score):
    scores = []
    result = []
    for s in score:
        scores.append(s)
        scores = sorted(scores, reverse=True)
        
        if len(scores) <= k:
            result.append(scores[-1])
        else:
            result.append(scores[k-1])
    return result