def solution(picture, k):
    result = []
    for row in picture:
        new = "".join([char*k for char in row])
        result += [new]*k
    return result