moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상, 하, 좌, 우

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    # (x, y) 기준 인접한 상, 하, 좌, 우 탐색
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if nx < 0 or nx >= n:
            continue
        if ny < 0 or ny >= m:
            continue
        if visited[nx][ny] == False and graph[nx][ny] == 0:
            dfs(nx, ny)

count = 0
for x in range(n):
    for y in range(m):
        if visited[x][y] == False and graph[x][y] == 0:
            dfs(x, y)
            count += 1
            
print(count)