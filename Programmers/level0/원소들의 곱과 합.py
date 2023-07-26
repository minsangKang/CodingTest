from functools import reduce

def solution(num_list):
    return 1 if reduce(lambda x, y: x*y, num_list) < sum(num_list)**2 else 0