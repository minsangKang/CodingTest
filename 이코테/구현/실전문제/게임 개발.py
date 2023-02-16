move = [(-1, 0), (0, 1), (1, 0), (0, -1)] #북, 동, 남, 서

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

moveCount = 1
while True:
    graph[x][y] = 2
    directionCount = 0
    for i in range(4):
        directionCount += 1
        direction -= 1
        direction %= 4
        
        nx = x + move[direction][0]
        ny = y + move[direction][1]
        
        if graph[nx][ny] == 0:
            x = nx
            y = ny
            moveCount += 1
            break
    
    if directionCount != 4:
        continue
    
    nx = x - move[direction][0]
    ny = y - move[direction][1]
    
    if graph[nx][ny] == 2:
        x = nx
        y = ny
    else:
        break
        
print(moveCount)