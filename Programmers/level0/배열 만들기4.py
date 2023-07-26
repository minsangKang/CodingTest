def solution(arr):
    i = 0
    answer = []
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif answer[-1] < arr[i]:
            answer.append(arr[i])
            i += 1
        else:
            answer.pop()
            
    return answer