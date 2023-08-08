def solution(n):
    # 몫을 기준으로 풀이
    return (n-1)//7 + 1
    # 조건을 기준으로 풀이
    result = 0
    while n > result*7:
        result += 1
    return result