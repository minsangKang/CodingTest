# 양방향 간선, 간선 비용 존재
# 간선비용 가장 높은 간선 제거 -> 두개의 마을로 쪼개짐
# 비용이 낮은 간선부터 연결, N-2개의 간선 선택 -> N-2개의 간선 비용 총합
def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    parent = min(find(parents, x), find(parents, y))
    parents[x] = parent
    parents[y] = parent

N, M = map(int, input().split())
parents = [0]*(N)
for i in range(N):
    parents[i] = i

edges = []
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a-1, b-1))
# 가장 비용이 큰 간선 제거 -> 두개의 마을로 설정
edges.sort()
edges.pop()
# 비용이 적은 간선부터 사이클이 발생하지 않는 N-2개의 간선 -> 총합
count = 0
totalCost = 0
for edge in edges:
    cost, a, b = edge
    cycle = find(parents, a) == find(parents, b)
    if cycle == False:
        union(parents, a, b)
        count += 1
        totalCost += cost
    
    if count == N-2:
        break

print(totalCost)
