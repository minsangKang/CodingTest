# s초가 지난 후에 x, y에 존재하는 바이러스의 종류를 출력
from collections import deque
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, k = map(int, input().split())

graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

s, x, y = map(int, input().split())

virus.sort()
q = deque(virus)
    
while q:
    v, time, i, j = q.popleft()
    if time == s:
        break
    for move in moves:
        nextX, nextY = i+move[0], j+move[1]
        if nextX < 0 or nextX >= n:
            continue
        if nextY < 0 or nextY >= n:
            continue
        if graph[nextX][nextY] == 0:
            graph[nextX][nextY] = v
            q.append((v, time+1, nextX, nextY))

print(graph[x-1][y-1])