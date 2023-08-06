def solution(score):
    score = [sum(score[i])/2 for i in range(len(score))]
    # 75, 70, 55, 65
    rank = sorted(score)[::-1]
    # 75, 70, 65, 55
    return [rank.index(num)+1 for num in score]