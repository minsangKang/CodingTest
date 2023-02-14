n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

result = 0
result += (numbers[n-1]*k) * (m // (k+1))
result += (numbers[n-1]) * (m % (k+1))
result += (numbers[n-2]) * (m // (k+1))

print(result)