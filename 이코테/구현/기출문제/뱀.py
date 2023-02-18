# 게임이 몇 초에 끝나는지 출력
from collections import deque
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
headDirection = 0
tailDirection = 0

n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]
apples = []
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2

l = int(input())
commands = deque()
for _ in range(l):
    x, c = input().split()
    commands.append((int(x), c))

time = 0
headX, headY = 0, 0
tailX, tailY = 0, 0
graph[headX][headY] = 1
commandIndex = 0
tailCommands = deque()
tailCommandIndex = -1
term = 1

while True:
    time += 1
    nextX, nextY = headX + move[headDirection][0], headY + move[headDirection][1]
    # 맵을 벗어난 경우
    if nextX < 0 or nextX >= n or nextY < 0 or nextY >= n:
        break
    # 몸과 만난 경우
    if graph[nextX][nextY] == 1:
        break
    # 머리 이동 반영
    headX, headY = nextX, nextY
    # 사과가 없는 곳으로 이동한 경우 꼬리 이동
    if graph[headX][headY] != 2:
        graph[tailX][tailY] = 0
        tailX, tailY = tailX + move[tailDirection][0], tailY + move[tailDirection][1]
    else:
        term += 1
    graph[headX][headY] = 1
    # 회전여부 확인
    if len(commands) != 0 and time == commands[0][0]:
        if commands[0][1] == 'D':
            headDirection += 1
        else:
            headDirection -= 1
        headDirection %= 4
        tailCommands.append((time+term, commands[0][1]))
        commands.popleft()
    # 꼬리 회전여부 확인
    if len(tailCommands) != 0 and time == tailCommands[0][0]:
        if tailCommands[0][1] == 'D':
            tailDirection += 1
        else:
            tailDirection -= 1
        tailDirection %= 4
        tailCommands.popleft()

print(time)