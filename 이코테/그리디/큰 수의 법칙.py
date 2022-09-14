N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

result = 0
result += (int(M//(K+1))*numbers[N-1]*K)
result += (int(M//(K+1))*numbers[N-2])
result += (int(M%(K+1))*numbers[N-1])

print(result)