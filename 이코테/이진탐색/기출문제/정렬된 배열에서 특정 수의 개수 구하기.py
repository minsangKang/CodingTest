#1: binarySearch 함수 직접구현
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))

def binarySearchLeft(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target and (mid == 0 or array[mid-1] < target):
            return mid
        elif target <= array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binarySearchRight(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target and (mid == len(array)-1 or array[mid+1] > target):
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

leftIndex = binarySearchLeft(nums, x, 0, n-1)
rightIndex = binarySearchRight(nums, x, 0, n-1)
if leftIndex == -1 or rightIndex == -1:
    print(-1)
else:
    print(rightIndex - leftIndex + 1)

#2: bisect 라이브러리 사용
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def count_by_range(array, leftValue, rightValue):
    leftIndex = bisect_left(array, leftValue)
    rightNextIndex = bisect_right(array, rightValue)
    return rightNextIndex - leftIndex

n, x = map(int, input().split())
nums = list(map(int, input().split()))
count = count_by_range(nums, x, x)

if count == 0:
    print(-1)
else:
    print(count)