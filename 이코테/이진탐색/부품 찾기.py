import sys
input = sys.stdin.readline

def binarySearch(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

def find(items, count, target):
    return binarySearch(items, 0, count-1, target) != -1

N = int(input())
items = list(map(int, input().split()))
items.sort()

M = int(input())
questions = list(map(int, input().split()))

for i in range(M):
    if find(items, N, questions[i]):
        print("yes", end=" ")
    else:
        print("no", end=" ")
print()