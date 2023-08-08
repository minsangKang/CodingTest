def solution(keyinput, board):
    dict = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    n, m = board[0]//2, board[1]//2
    x, y = 0, 0
    for key in keyinput:
        nx, ny = x+dict[key][0], y+dict[key][1]
        if nx < -n or nx > n:
            continue
        if ny < -m or ny > m:
            continue
        x, y = nx, ny
    return [x, y]