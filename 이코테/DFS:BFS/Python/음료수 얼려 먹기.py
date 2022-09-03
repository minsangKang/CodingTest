def dfs(row, column, n, m, visited, graph):
    visited[row][column] = True
    if row-1 >= 0 and visited[row-1][column] == False and graph[row-1][column] == 0:
        dfs(row-1, column, n, m, visited, graph)
    if column-1 >= 0 and visited[row][column-1] == False and graph[row][column-1] == 0:
        dfs(row, column-1, n, m, visited, graph)
    if row+1 <= n-1 and visited[row+1][column] == False and graph[row+1][column] == 0:
        dfs(row+1, column, n, m, visited, graph)
    if column+1 <= m-1 and visited[row][column+1] == False and graph[row][column+1] == 0:
        dfs(row, column+1, n, m, visited, graph)


def solution(n, m, graph):
    visited = [[False] * m for i in range(n)]
    count = 0

    for row in range(n):
        for column in range(m):
            if graph[row][column] == 0 and visited[row][column] != True:
                count += 1
                dfs(row, column, n, m, visited, graph)
    
    return count

n, m = map(int, input().split())
map = []
for row in range(n):
    line = [int(x) for x in list(input())]
    map.append(line)

answer = solution(n, m, map)
print(answer)