# 두 사람이 서로 다른 무게의 공을 고르는 경우의 수
n, m = map(int, input().split())
balls = list(map(int, input().split()))
count = [0] * (m+1)
for ball in balls:
    count[ball] += 1

result = 0
for i in range(1, m):
    if count[i] == 0:
        continue
    first = count[i]
    second = n - count[i]
    result += (first * second)
    n -= count[i]

print(result)