from collections import deque
# x로부터 출발하여 최단 거리가 정확히 k인 모든 도시의 번호를 출력
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)

visited = [0] * n
q = deque([x-1])

results = []
while q:
    now = q.popleft()
    
    for node in graph[now]:
        if visited[node] == 0:
            visited[node] = visited[now]+1
            if visited[node] == k:
                results.append(node)
            q.append(node)

results.sort()
if len(results) == 0:
    print(-1)
else:
    for i in results:
        print(i+1)