import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 다익스트라
def dijkstra(graph, start):
	distance = [INF] * (len(graph) + 1)
	distance[start] = 0
	q = [] # (dist, to)
	heapq.heappush(q, (0, start))

	while q:
		currentDist, currentNodeNum = heapq.heappop(q)
		# 현재 노드가 이미 처리된 적이 있는 노드라면 무시
		if distance[currentNodeNum] < currentDist:
			continue
		# 현재 노드와 연결된 다른 인접한 노드들을 확인
		for node in graph[currentNodeNum]:
			nodeNum = node[0]
			nodeCost = node[1]
			newDist = currentDist + nodeCost
			# 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
			if newDist < distance[nodeNum]:
				distance[nodeNum] = newDist
				heapq.heappush(q, (newDist, nodeNum))

	return distance


n, m = map(int, input().split()) # n: 노드수, m: 간선수
start = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
	node, to, cost = map(int, input().split())
	graph[node].append((to, cost))

distance = dijkstra(graph, start)
for i in range(1, n+1):
	if distance[i] == INF:
		print("INF")
	else:
		print(distance[i])