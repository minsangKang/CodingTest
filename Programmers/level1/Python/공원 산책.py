def solution(park, routes):
    dict = { 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1), 'S': (1, 0) }
    y, x = 0, 0
    h, w = len(park), len(park[0])
    # 시작지점 search
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                y, x = i, j
                break
    
    for route in routes:
        print(y, x)
        op, n = route.split()
        ty, tx = y, x # 임시 y, x 저장
        canGo = True
        for i in range(1, int(n)+1):
            ty, tx = y + dict[op][0]*i, x + dict[op][1]*i
            # 벗어나는지, 장애물 확인
            if ty < 0 or ty >= h or tx < 0 or tx >= w:
                canGo = False
                break
            if park[ty][tx] == 'X':
                canGo = False
                break
        # 이동
        if canGo:
            y, x = ty, tx
    return [y, x]