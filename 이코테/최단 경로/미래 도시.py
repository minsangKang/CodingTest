# 시작 노드: 1, 간선 비용: 1
# 1 -> K -> X 최소시간을 계산
INF = int(1e9)

def floydWarshall(graph, N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

N, M = map(int, input().split())
graph = [[INF]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    s, t = map(int, input().split())
    graph[s-1][t-1] = 1
    graph[t-1][s-1] = 1    

X, K = map(int, input().split())
floydWarshall(graph, N)

first = graph[0][K-1]
second = graph[K-1][X-1]
canGo = first != INF and second != INF
print(first + second if canGo else -1)