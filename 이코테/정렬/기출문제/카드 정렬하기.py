import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

sum = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    newValue = one + two
    sum += newValue
    heapq.heappush(heap, newValue)

print(sum)