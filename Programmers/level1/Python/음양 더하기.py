def solution(absolutes, signs):
    result = 0
    for n, sign in zip(absolutes, signs):
        result += n if sign else -n
    return result