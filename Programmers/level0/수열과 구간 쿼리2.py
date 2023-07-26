def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        targets = list(filter(lambda x: x > k, arr[s:e+1]))
        answer.append(-1 if len(targets) == 0 else min(targets))
    return answer