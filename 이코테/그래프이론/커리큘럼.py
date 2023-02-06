# N개의 강의 각각 걸리는 최소시간 구하기
# N = int(input())
# times = [0]*(N+1)

# for i in range(1, N+1):
#     inputs = list(map(int, input().split()))
#     if len (inputs) == 2:
#         times[i] = inputs[0]
#     else:
#         for num in inputs[1:len(inputs)-1]:
#             times[i] = max(times[i], times[num]+inputs[0])

# for i in range(1, N+1):
#     print(times[i])

from collections import deque
import copy

v = int(input())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]
time = [0]*(v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    for x in data[1:-1]:
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()