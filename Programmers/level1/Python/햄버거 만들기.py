def solution(ingredient):
    stack = []
    count = 0
    for i in ingredient:
        stack.append(i)
        
        if stack[-4:] == [1, 2, 3, 1]:
            count += 1
            # 슬라이싱 대신 del(또는 pop() 네번)을 사용해야 시간초과 해결
            del stack[-4:]

    return count