def solution(array, n):
    # sort의 1순위, 2순위 tuple 사용
    array.sort(key=lambda x: (abs(x-n), x))
    return array[0]

    # 1차풀이방법
    array.sort()
    index = array.index(n)
    
    if index == 0:
        return array[1]
    elif index == len(array)-1:
        return array[-2]
    
    distLeft = array[index]-array[index-1]
    distRight = array[index+1]-array[index]
    
    if distRight < distLeft:
        return array[index+1]
    else:
        return array[index-1]