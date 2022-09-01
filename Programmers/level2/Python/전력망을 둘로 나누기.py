import copy

def getNodeCount(map, startNode):
    # startNode 부터 시작해 DFS 로 연결된 node수 확인
    visited = []
    stack = [startNode]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            for i in range(len(map[0])):
                if map[n][i] != 0:
                    stack.append(i)
    
    return len(visited)

def removeWireAndGetAbs(map, wire):
    # wire 제거
    map[wire[0]-1][wire[1]-1] = 0
    map[wire[1]-1][wire[0]-1] = 0
    # def 로 각각의 node수 확인
    group1Count = getNodeCount(map, wire[0]-1)
    group2Count = getNodeCount(map, wire[1]-1)

    return abs(group1Count - group2Count)

# wire 하나를 선택, 각 node 를 기준으로 bfs -> set 넣어 개수 -> 절대갓 비교
# 절대값 min 값 반환
def solution(n, wires):
    # n*n map 생성
    map = [[0]*n for i in range(n)]
    # wire 연결
    for wire in wires:
        map[wire[0]-1][wire[1]-1] = 1
        map[wire[1]-1][wire[0]-1] = 1
    # wire 제거 및 개수 반환
    minAbs = n
    for wire in wires:
        minAbs = min(minAbs, removeWireAndGetAbs(copy.deepcopy(map), wire))

    return minAbs

answer = solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
print(answer)