def solution(date1, date2):
    date1 = int("".join(map(str, date1)))
    date2 = int("".join(map(str, date2)))
    return int(date1 < date2)