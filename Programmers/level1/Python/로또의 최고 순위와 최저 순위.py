def solution(lottos, win_nums):
    wins = set(win_nums)&set(lottos)
    zeroCount = lottos.count(0)
    choice = set(win_nums)-wins
    
    score = len(wins)
    maxScore = score + min(len(choice), zeroCount)
    
    maxRank = 7-maxScore if maxScore > 1 else 6
    minRank = 7-score if score > 1 else 6
    return [maxRank, minRank]