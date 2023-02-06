n, m = map(int, input().split())

maxCard = -1
for _ in range(n):
    row = list(map(int, input().split()))
    maxCard = max(maxCard, min(row))
print(maxCard)