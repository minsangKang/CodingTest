import sys
import heapq
input = sys.stdin.readline
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

INF = int(1e9)
def dijkstra(graph, n, x, y):
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = graph[x][y]
    q = []
    heapq.heappush(q, (graph[x][y], x, y))

    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue

        for move in moves:
            nx = x+move[0]
            ny = y+move[1]
            
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue

            cost = graph[nx][ny]
            newCost = dist + cost
            if newCost < distance[nx][ny]:
                distance[nx][ny] = newCost
                heapq.heappush(q, (newCost, nx, ny))

    return distance

t = int(input())
for _ in range(t):
    n = int(input())

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = dijkstra(graph, n, 0, 0)
    
    print(distance[n-1][n-1])
