import sys
input = sys.stdin.readline

n = int(input())
locations = list(map(int, input().split()))
locations.sort()

# 중앙위치값이 거리합산의 최솟값이 된다
print(locations[(n-1) // 2])