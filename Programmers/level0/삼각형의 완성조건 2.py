def solution(sides):
    a, b = sides
    targets = list(range(abs(a-b)+1, a+b))
    count = 0
    for c in targets:
        sumValue = a+b+c
        maxValue = max(a, b, c)
        minValue = min(a, b, c)
        
        if maxValue < sumValue - maxValue:
            count += 1
    return count
        