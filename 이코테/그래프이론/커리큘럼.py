# N개의 강의 각각 걸리는 최소시간 구하기
N = int(input())
times = [0]*(N+1)
indegrees = [0]*(N+1)

for i in range(1, N+1):
    inputs = list(map(int, input().split()))
    if len (inputs) == 2:
        times[i] = inputs[0]
    else:
        for num in inputs[1:len(inputs)-1]:
            times[i] = max(times[i], times[num]+inputs[0])

for i in range(1, N+1):
    print(times[i])

