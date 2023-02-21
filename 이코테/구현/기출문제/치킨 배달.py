# 0: 빈칸, 1: 집, 2: 치킨집
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리: 모든 집의 치킨 거리의 합
# 최대 M개의 치킨집을 골랐을 때 도시의 치킨 거리의 최솟값
from itertools import combinations

def dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

NONE, HOUSE, CHICK = 0, 1, 2
n, m = map(int, input().split())
house = []
chick = []
for r in range(n):
    row = list(map(int, input().split()))
    for c in range(n):
        if row[c] == HOUSE:
            house.append((r, c))
        elif row[c] == CHICK:
            chick.append((r, c))
# 도시의 치킨 거리 최솟값
minDist = int(1e9)
for case in list(combinations(chick, m)):
    # 선택된 m개의 치킨집기준 도시의 치킨 거리 최솟값
    distSum = 0
    for a in house:
        # 특정 집의 치킨 거리 최솟값
        houseDist = int(1e9)
        for b in case:
            temp = dist(a, b)
            houseDist = min(houseDist,  temp)
        # 특정 집의 치킨 거리 최솟값이 구해지면 도시의 치킨 거리 최솟값에 반영
        distSum += houseDist
    # 선택된 m개의 치킨집기준 도시의 치킨 거리 최솟값이 구해지면 도시의 치킨 거리 최솟값에 반영
    minDist = min(minDist, distSum)

print(minDist)
        
