INF = 10001
n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
moneys.sort()

dp = [INF]*(m+1)
dp[0] = 0

for money in moneys:
    for i in range(money, m+1):
        if dp[i-money] != INF:
            dp[i] = min(dp[i], dp[i-money]+1)
        
print(dp[m] if dp[m] != INF else -1)