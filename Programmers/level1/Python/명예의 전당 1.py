def solution(k, score):
    result = []
    arr = []
    for s in score:
        arr.append(s)
        arr = sorted(arr)
        if len(arr) <= k:
            result.append(arr[0])
        else:
            result.append(arr[-k])
    return result