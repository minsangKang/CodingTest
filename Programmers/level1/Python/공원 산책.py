def solution(park, routes):
    move = {'E':(0,1), 'W':(0,-1), 'N':(-1,0), 'S':(1,0)}
    h, w = len(park), len(park[0])
    y, x = 0, 0
    # 시작위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                y, x = i, j
    # 이동
    for route in routes:
        direct, length = route.split()[0], int(route.split()[1])
        tempY, tempX = y, x
        isBreak = False
        
        for i in range(length):
            ny, nx = tempY+move[direct][0], tempX+move[direct][1]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                isBreak = True
                break
            if park[ny][nx] == 'X':
                isBreak = True
                break
            tempY, tempX = ny, nx
        if isBreak == False:
            y, x = tempY, tempX
    return [y, x]
    