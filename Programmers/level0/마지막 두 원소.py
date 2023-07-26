def solution(num_list):
    last = num_list[-1]
    second = num_list[-2]
    return num_list + [last-second] if last > second else num_list + [last*2]