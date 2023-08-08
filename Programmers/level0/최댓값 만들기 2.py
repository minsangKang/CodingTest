def solution(numbers):
    # 2개 이상이므로 끝 두개의 곱끼리 비교
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    # plus, minus 따로 분류한 풀이
    plusnumbers = sorted(filter(lambda x: x>0, numbers))
    minusnumbers = sorted(filter(lambda x: x<0, numbers))
    maxValue = numbers[0]*numbers[1]
    if len(plusnumbers) > 1:
        maxValue = max(maxValue, plusnumbers[-1]*plusnumbers[-2])
    if len(minusnumbers) > 1:
        maxValue = max(maxValue, minusnumbers[0]*minusnumbers[1])
    
    return maxValue