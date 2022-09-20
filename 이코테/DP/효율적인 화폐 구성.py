INF = 10001
N, M = map(int, input().split())
moneys = []
for i in range(N):
    moneys.append(int(input()))
moneys.sort()

dp = [INF]*(M+1)
dp[0] = 0

# 작은 화폐부터 시작하여 채운다
for m in moneys:
    count = 1
    while(m*count <= M):
        dp[m*count] = min(dp[m*count] ,dp[m*(count-1)] + 1)
        count += 1

print(dp[M] if dp[M] != INF else -1)