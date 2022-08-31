# 가로: 모든 w, h 중 max
# 세로: (w, h) 중 min 값들의 max
def solution(sizes):
    maxWidth = 0
    maxHeight = 0
    for size in sizes:
        maxWidth = max(maxWidth, max(size[0], size[1]))
        maxHeight = max(maxHeight, min(size[0], size[1]))
    
    answer = maxWidth * maxHeight
    return answer

answer = solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
print(answer)
