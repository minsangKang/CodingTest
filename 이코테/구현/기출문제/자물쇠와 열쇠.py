# 열쇠로 좌물쇠를 열 수 있으면 true, 없으면 false 를 return
import copy

# n*m 행렬 90 회전 -> m*n 행렬 반환                
def rotation(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotated = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            rotated[j][(n-1)-i] = matrix[i][j]
            
    return rotated

# lock 중앙부분 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    # 4가지 방향에 대해서 확인
    for _ in range(4):
        key = rotation(key)
        for x in range(2*n):
            for y in range(2*n):
                check_lock = copy.deepcopy(new_lock)
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        check_lock[x+i][y+j] += key[i][j]
                
                if check(check_lock) == True:
                    return True
        
    return False