# 만들 수 없는 최솟값
n = int(input())
coins = list(map(int, input().split()))
coins.sort()
# 1 1 2 3 9
target = 1
for coin in coins:
    if coin <= target:
        target += coin
    else:
        break

print(target)
