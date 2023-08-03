def solution(n):
    result = [[-1]*n for _ in range(n)]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, direction = 0, 0, 0
    # 현재 방향으로 쭉 이동 (어디까지? -1인 경우까지)
    for i in range(1, n*n+1):
        result[y][x] = i
        # 맨 밖같인 경우 outof range 확인 후 회전
        ny, nx = y+move[direction][0], x+move[direction][1]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            direction = (direction+1)%4
            y, x = y+move[direction][0], x+move[direction][1]
        # 다음 위치가 -1인 경우 회전
        elif result[ny][nx] != -1:
            direction = (direction+1)%4
            y, x = y+move[direction][0], x+move[direction][1]
        else:
            y, x = ny, nx
            
    return result