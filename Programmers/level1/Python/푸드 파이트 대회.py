def solution(food):
    left = ""
    for idx, count in enumerate(food):
        if idx == 0:
            continue
        count = (count//2)*2
        left += str(idx)*(count//2)
    
    return left+"0"+left[::-1]