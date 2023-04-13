# 최소시간, 이동 cost 가 동일: BFS로 접근
# BFS: deque + 이동가능한 좌표값들 + 이동가능한지 체킹 + cost
# 이동 가능한 좌표값들을 반환하는 함수가 핵심

from collections import deque

# 현재 로봇위치 -> 움직일 수 있는 모든 좌표 리스트 반환
def getNextPoints(points, newBoard):
    canMoves = []
    # 집합 -> 리스트로 변환
    points = list(points)
    lx, ly = points[0][0], points[0][1]
    rx, ry = points[1][0], points[1][1]
    
    # 상, 하, 좌, 우 이동 확인
    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_lx, next_ly = lx+move[0], ly+move[1]
        next_rx, next_ry = rx+move[0], ry+move[1]
        # 이동 가능한지 확인 후 canMoves 내 추가
        if newBoard[next_lx][next_ly] == 0 and newBoard[next_rx][next_ry] == 0:
            canMoves.append({(next_lx, next_ly), (next_rx, next_ry)})
            
    # 가로 -> 세로 회전 확인
    if lx == rx:
        # 위, 아래방향 확인
        for move in [1, -1]:
            if newBoard[lx+move][ly] == 0 and newBoard[rx+move][ry] == 0:
                # 좌측 고정, 우측 위, 아래 회전
                canMoves.append({(lx, ly), (lx+move, ly)})
                # 우측 고정, 좌측 위, 아래 회전
                canMoves.append({(rx+move, ry), (rx, ry)})
                
    # 세로 -> 가로 회전 확인
    if ly == ry:
        # 좌, 우방향 확인
        for move in [-1, 1]:
            if newBoard[lx][ly+move] == 0 and newBoard[rx][ry+move] == 0:
                # 위 고정, 아래 좌, 우 회전
                canMoves.append({(lx, ly), (lx, ly+move)})
                # 아래 고정, 위 좌, 우 회전
                canMoves.append({(rx, ry+move), (rx, ry)})
    
    # 최종 이동가능한 Points 집합 리스트 반환
    return canMoves

def solution(board):
    # 테두리 1로 채운 board 로 변환
    n = len(board)
    newBoard = [[1]*(n+2) for _ in range(n+2)]
    for x in range(n):
        for y in range(n):
            newBoard[x+1][y+1] = board[x][y]
    
    # 이동한 위치값들
    startPoints = {(1, 1), (1, 2)}
    visitedPoints = [startPoints]
    # deque: points, cost 값
    q = deque([(startPoints, 0)])
    
    while q:
        # 현재 로봇위치가 n, n 에 닿은 경우
        points, cost = q.popleft()
        if (n, n) in points:
            return cost
        
        # 로봇이 움직일 수 있는 모든 위치 deque 에 추가
        for nextPoints in getNextPoints(points, newBoard):
            if nextPoints not in visitedPoints:
                q.append((nextPoints, cost+1))
                visitedPoints.append(nextPoints)
    return 0