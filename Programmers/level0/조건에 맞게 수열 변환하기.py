import copy

def solution(arr):
    before = copy.deepcopy(arr)
    x = 0
    while True:
        for i in range(len(arr)):
            num = arr[i]
            if num >= 50 and num%2 == 0:
                arr[i] //= 2
            elif num < 50 and num%2 == 1:
                arr[i] = arr[i]*2+1
        
        if before == arr:
            return x
        before = copy.deepcopy(arr)
        x += 1