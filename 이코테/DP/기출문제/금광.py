import sys
import copy
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    index = 0
    graph = []
    for i in range(n):
        graph.append(array[index:index+m])
        index += m

    # DP 시작
    dp = copy.deepcopy(graph)
    maxValue = 0
    for j in range(1, m):
        for i in range(n):
            dp[i][j] = max(dp[i][j], dp[i][j-1] + graph[i][j])
            if i-1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + graph[i][j])
            if i+1 < n:
                dp[i][j] = max(dp[i][j], dp[i+1][j-1] + graph[i][j])
            maxValue = max(maxValue, dp[i][j])

    for i in range(n):
        for j in range(m):
            print(dp[i][j], end=" ")
        print()
    print()

    print(maxValue)


