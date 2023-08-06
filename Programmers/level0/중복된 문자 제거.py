def solution(my_string):
    result = []
    for char in my_string:
        if char not in result:
            result.append(char)
    return "".join(result)
            