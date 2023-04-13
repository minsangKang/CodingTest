import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

def getSum(h):
    sum = 0
    for i in heights:
        if i > h:
           sum += (i - h)
    return sum

def paramatric_search(start, end, sum):
    temp = 0
    while start <= end:
        mid = (start + end) // 2
        currentSum = getSum(mid)
        if currentSum == sum:
            return mid
        elif currentSum < sum:
            end = mid - 1
        else:
            temp = mid
            start = mid + 1
    return temp

print(paramatric_search(min(heights), max(heights), m))