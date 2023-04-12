# 안전 영역 크기의 최댓값 출력
# 0: 빈칸, 1: 벽, 2: 바이러스
from itertools import combinations
import copy
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

n, m = map(int, input().split())
graph = []
empty = []
virus = []
for x in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for y in range(m):
        if row[y] == 0:
            empty.append((x, y))
        elif row[y] == 2:
            virus.append((x, y))

# 안전 영역의 크기
safeCount = 0
global emptyCount
emptyCount = len(empty)

# 바이러스 DFS 함수
def dfs(graph, x, y):
    global emptyCount
    for move in moves:
        nextX, nextY = x+move[0], y+move[1]
        if nextX < 0 or nextX >= n:
            continue
        if nextY < 0 or nextY >= m:
            continue
        # 빈칸인 경우 바이러스 퍼짐
        if graph[nextX][nextY] == 0:
            graph[nextX][nextY] = 2
            emptyCount -= 1
            dfs(graph, nextX, nextY)

# 빈칸 세곳을 조합으로 선택
for case in combinations(empty, 3):
    checkGraph = copy.deepcopy(graph)
    for x, y in case:
        # 빈칸 세곳을 벽으로 설정
        checkGraph[x][y] = 1
    # 남은 빈칸수
    emptyCount = len(empty)-3
    # 바이러스 DFS 진행
    for x, y in virus:
        dfs(checkGraph, x, y)
    # 최댓값 반영
    safeCount = max(safeCount, emptyCount)

print(safeCount)