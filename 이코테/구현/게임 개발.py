# 0: 육지, 1: 바다, 2: 가본 육지
# 회전: direction++%4
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

moveCount = 1
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = []
for row in range(n):
    graph.append(list(map(int, input().split())))

def validPosition(poX, poY):
    return poX >= 0 and poX < m and poY >= 0 and poY < n

while(True):
    # 이동 후
    rotationCount = 0
    graph[x][y] = 2
    # 회전하며 이동 확인
    for i in range(4):
        rotationCount += 1
        direction += 1
        direction %= 4

        nextX = x + move[direction][0]
        nextY = y + move[direction][1]

        if validPosition(nextX, nextY) and graph[nextX][nextY] == 0:
            x = nextX
            y = nextY
            moveCount += 1
            break
        else:
            continue
    # 4방향 모두 확인 이후
    if rotationCount != 4:
        continue
    
    backDirection = (direction + 2)%4
    backX = x + move[backDirection][0]
    backY = y + move[backDirection][1]

    if validPosition(backX, backY) and graph[backX][backY] == 2:
        x = backX
        y = backY
    else:
        break

print(moveCount)

