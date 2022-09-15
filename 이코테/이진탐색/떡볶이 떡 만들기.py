import sys
input = sys.stdin.readline

def totalSum(heights, height):
    sum = 0
    for h in heights:
        if h > height:
            sum += (h-height)
    return sum

def binarySearchHeight(heights, start, end, overSum):
    result = 0
    while start <= end:
        midHeight = (start+end)//2
        sum = totalSum(heights, midHeight)
        if sum == overSum:
            return midHeight
        elif sum < overSum:
            end = midHeight-1
        else:
            result = midHeight
            start = midHeight+1
    return result

# 자투리 합산: M 이상이 되기 위한 최대 H 구하기
N, M = map(int, input().split())
heights = list(map(int, input().split()))

# H 최소높이, 최대높이 값을 구한 후 binarySearch 를 통해 height 값을 찾는다
finalHeight = binarySearchHeight(heights, min(heights), max(heights), M)
print(finalHeight)