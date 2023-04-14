import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], cost)

for c in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
                    

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()