def solution(sizes):
    return max([max(s) for s in sizes]) * max([min(s) for s in sizes])