# T: 선생, S: 학생, O: 장애물
# 장애물을 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력
from itertools import combinations
import copy
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 학생들이 모두 피해질 수 있는지 여부 함수
def canAvoid(graph, teachers):
    for i, j in teachers:
        for move in moves:
            x, y = i, j
            # 한 방향에 대해 움직일 수 있을때까지 확인
            while True:
                nextX, nextY = x+move[0], y+move[1]
                # 움직일 수 없는 경우 다음방향 탐색으로 이동
                if nextX < 0 or nextX >= n:
                    break
                if nextY < 0 or nextY >= n:
                    break
                # 장애물인 경우 다음방향 탐색으로 이동
                if graph[nextX][nextY] == 'O':
                    break
                # 학생을 만난 경우 종료
                elif graph[nextX][nextY] == 'S':
                    return False
                x, y = nextX, nextY
    return True

n = int(input())
graph = []
empty = []
teachers = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'X':
            empty.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))

# 빈공간 중 3가지 조합
can = False
for locations in combinations(empty, 3):
    checkGraph = copy.deepcopy(graph)
    for i, j in locations:
        checkGraph[i][j] = 'O'
    
    # 학생들 모두 피해지는 경우 종료
    if canAvoid(checkGraph, teachers):
        can = True
        break

print("YES" if can else "NO")
