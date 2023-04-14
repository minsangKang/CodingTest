from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n)]
indegree = [0] * n
time = [0] * n

for i in range(n):
    inputs = list(map(int, input().split()))
    time[i] = inputs[0]
    for j in inputs[1:-1]:
        graph[j-1].append(i)
        indegree[i] += 1
        
def topology_sort():
    q = deque()
    result = copy.deepcopy(time)
    
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for node in graph[now]:
            result[node] = max(result[node], result[now] + time[node])
            indegree[node] -= 1
            
            if indegree[node] == 0:
                q.append(node)
                
    return result
                
result = topology_sort()
for t in result:
    print(t)