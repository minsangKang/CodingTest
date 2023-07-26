def solution(my_string, queries):
    for s, e in queries:
        my_string = my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    return my_string