# 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 출력
# 인접한 두 나라의 수가 l 이상 r 이하인 경우 인구이동
from collections import deque
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs(i, j):
    united = []
    united.append((i, j))
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    sum = 0

    while q:
        x, y = q.popleft()
        for move in moves:
            nx, ny = x+move[0], y+move[1]
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue
            diff = abs(graph[nx][ny] - graph[x][y])
            if l <= diff <= r and visited[nx][ny] == False:
                q.append((nx, ny))
                united.append((nx, ny))
                visited[nx][ny] = True
                sum += graph[nx][ny]

    if sum == 0:
        return False
    
    newValue = sum // len(united)
    for x, y in united:
        graph[x][y] = newValue
    return True

count = 0
while True:
    moved = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                moved = bfs(i, j)
    
    if moved:
        count += 1
        visited = [[False]*n for _ in range(n)]
    else:
        break

print(count)
                    