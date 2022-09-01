def solution(brown, yellow):
    widthAndHeightSum = (brown-4)//2
    widthAndHeightMultiply = yellow
    
    for width in range(1, widthAndHeightSum):
        height = widthAndHeightSum - width
        if (width >= height) and (width*height == widthAndHeightMultiply):
            return [width+2, height+2]

answer = solution(8, 1)
print(answer)