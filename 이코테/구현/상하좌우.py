move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
commend = ["U", "L", "D", "R"]

n = int(input())
actions = list(input().split())

x, y = 1, 1
for i in range(len(actions)):
    moveDirection = commend.index(actions[i])
    nextX = x + move[moveDirection][0]
    nextY = y + move[moveDirection][1]

    if nextX >= 1 and nextY <= n and nextY >= 1 and nextY <= n:
        x = nextX
        y = nextY
print(x, y)
