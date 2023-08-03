def solution(arr):
    rowCount = len(arr)
    columnCount = len(arr[0])
    
    if columnCount > rowCount:
        arr += [[0]*columnCount for _ in range(columnCount - rowCount)]
    else:
        for i in range(rowCount):
            arr[i] += [0]*(rowCount - columnCount)
            
    return arr