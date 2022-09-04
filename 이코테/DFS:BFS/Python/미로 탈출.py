from collections import deque
# 1: 움직일 수 있는 칸
# 최소로 움직일 수 있는 거리 -> BFS로 한칸씩 증가하며 확인
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def bfs(n, m, graph):
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nextX = x + move[i][0]
            nextY = y + move[i][1]

            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                continue
            if graph[nextX][nextY] == 1:
                graph[nextX][nextY] = graph[x][y]+1
                queue.append((nextX, nextY))
    
    return graph[n-1][m-1]


def solution(n, m, graph):
    return bfs(n, m, graph)

n, m = map(int, input().split())
graph = []
for row in range(n):
    line = [int(x) for x in list(input())]
    graph.append(line)

answer = solution(n, m, graph)
print(answer)