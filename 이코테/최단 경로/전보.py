# 유향그래프, 간선 비용 존재
# 출발: C / 수신받는 도시수, 총 시간
# 출발 부터 연결된 노드까지의 최단거리 -> 다익스트라 알고리즘
import heapq
INF = int(1e9)

def dijkstra(graph, times, start):
    times[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        time, node = heapq.heappop(q)
        
        if times[node] < time:
            continue

        for n in graph[node]:
            nodeTime, nodeNum = n
            newTime = time + nodeTime
            if newTime < times[nodeNum]:
                times[nodeNum] = newTime
                heapq.heappush(q, (newTime, nodeNum))


N, M, start = map(int, input().split())

graph = [[] for i in range(N)]
for i in range(M):
    s, t, time = map(int, input().split())
    graph[s-1].append((time, t-1))

times = [INF]*N
dijkstra(graph, times, start-1)

nodeCount = 0
maxTime = -1

for n in range(N):
    if times[n] != INF:
        nodeCount += 1
        maxTime = max(maxTime, times[n])
print(nodeCount-1, maxTime)
    