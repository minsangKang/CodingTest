from collections import deque
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

# 사과 정보 입력
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 회전 정보 입력
rotations = []
l = int(input())
for _ in range(l):
    x, c = input().split()
    rotations.append((int(x), c))

# 시뮬레이션 설정
headX, headY = 1, 1
graph[headX][headY] = 2
direction = 0
time = 0
index = 0 # rotation 인텍스
q = deque()
q.append((headX, headY)) # 뱀이 차지하고 있는 위치 정보

while True:
    nextX = headX + move[direction][0]
    nextY = headY + move[direction][1]
    time += 1
    
    # 이동불가 or 몸통과 만난 경우 종료
    if nextX < 1 or nextX > n:
        break
    if nextY < 1 or nextY > n:
        break
    if graph[nextX][nextY] == 2:
        break

    # 사과가 위치한 경우 머리이동
    if graph[nextX][nextY] == 1:
        headX, headY = nextX, nextY
        graph[headX][headY] = 2
        q.append((headX, headY))

    # 사과가 위치하지 않은 경우 머리이동 후 꼬리위치 제거
    if graph[nextX][nextY] == 0:
        headX, headY = nextX, nextY
        graph[headX][headY] = 2
        q.append((headX, headY))

        tailX, tailY = q.popleft()
        graph[tailX][tailY] = 0
    
    # 회전시간인지 여부 확인
    if index < l and rotations[index][0] == time:
        if rotations[index][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        index += 1

print(time)