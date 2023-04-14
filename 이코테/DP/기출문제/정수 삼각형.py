import sys
import copy

n = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i+1):
        graph[i][j] = row[j]

dp = copy.deepcopy(graph)
maxValue = dp[0][0]

for x in range(1, n):
    for y in range(n):
        dp[x][y] = max(dp[x][y], dp[x-1][y] + graph[x][y])
        if y-1 >= 0:
            dp[x][y] = max(dp[x][y], dp[x-1][y-1] + graph[x][y])
        maxValue = max(maxValue, dp[x][y])

print(maxValue)