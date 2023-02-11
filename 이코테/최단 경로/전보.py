import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x-1].append((y-1, z))
    
def dijkstra(start, n):
    distance = [INF] * n
    distance[start-1] = 0
    q = []
    heapq.heappush(q, (0, start-1))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for n in graph[now]:
            node = n[0]
            cost = n[1]
            newDist = dist + cost
            
            if newDist < distance[node]:
                distance[node] = newDist
                heapq.heappush(q, (newDist, node))
                
    return distance

distance = dijkstra(c, n)

nodeCount = 0
maxTime = 0
for i in range(n):
    if distance[i] != INF:
        nodeCount += 1
        maxTime = max(maxTime, distance[i])
        
print(nodeCount-1, maxTime)