from collections import deque
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상, 하, 좌, 우

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs():
    que = deque()
    que.append((0, 0))
    
    while que:
        x, y = que.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                que.append((nx, ny))

bfs()
print(graph[n-1][m-1])