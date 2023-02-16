import sys
input = sys.stdin.readline

move = dict(L=(0, -1), R=(0, 1), U=(-1, 0), D=(1, 0))

n = int(input())
inputs = input().split()

x, y = 1, 1
for command in inputs:
    nx = x + move[command][0]
    ny = y + move[command][1]
    
    if nx < 1 or nx > n:
        continue
    if ny < 1 or ny > n:
        continue
        
    x, y = nx, ny
    
print(x, y)