import sys
from collections import deque
input = sys.stdin.readline
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상 하 좌 우 인접나라 확인
def process(graph, x, y):
    check[x][y] = True
    contry = [(x, y)]
    q = deque(contry)
    sum = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for move in moves:
            nx, ny = x+move[0], y+move[1]
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue

            if check[nx][ny] == False:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    check[nx][ny] = True
                    contry.append((nx, ny))
                    q.append((nx, ny))
                    sum += graph[nx][ny]
                    count += 1
    # contry 계산
    for i, j in contry:
        graph[i][j] = sum // count
    
    return count != 1

# 인구 이동 횟수
moveCount = 0

while True:
    # 개방 확인 여부
    check = [[False]*n for _ in range(n)]
    # 개방 여부
    isMoving = False
    # 모든 나라 국경선 개방가능 여부 확인
    for x in range(n):
        for y in range(n):
            if check[x][y] == False:
                isMoving |= process(graph, x, y)
    
    # 개방된 나라가 없는 경우
    if isMoving == False:
        break
    moveCount += 1

print(moveCount)