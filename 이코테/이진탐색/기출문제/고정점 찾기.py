import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def binarySearch(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(binarySearch(nums, 0, n-1))

# middle: 중앙인덱스값 (2)
# nums[middle]: 중앙값 (1)
# 값(1) < 인덱스(2)
# 값을 높여야 하므로 위쪽으로 탐색
# middle: 3
# nums[middle]: 3
# 같음 -> 반환
# 
# mid: 3
# nums[3]: 8
# 값(8) > 인덱스(3) 
# 값을 낮춰야 하므로 아래쪽으로 탐색
