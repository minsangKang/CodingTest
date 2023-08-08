def setNoneSafe(board, row, column, n):
    for i in range(row-1, row+2):
        if i < 0 or i >= n:
                continue
        for j in range(column-1, column+2):
            if j < 0 or j >= n:
                continue
            if board[i][j] == 0:
                board[i][j] = 2

def solution(board):
    n = len(board)
    for row in range(n):
        for column in range(n):
            if board[row][column] == 1:
                # 지뢰 발견, 주위 2로 설정
                setNoneSafe(board, row, column, n)
                
    return sum(board, []).count(0)