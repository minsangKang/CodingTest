def solution(l, r):
    answer = []
    for num in range(l, r+1):
        nums = set(map(int, str(num)))
        if nums == set([0]) or nums == set([5]) or nums == set([0, 5]):
            answer.append(num)
    return answer if len(answer) > 0 else [-1]