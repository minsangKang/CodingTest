def solution(wallpaper):
    luy, lux = len(wallpaper), len(wallpaper[0])
    rdy, rdx = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                luy, lux = min(luy, i), min(lux, j)
                rdy, rdx = max(rdy, i), max(rdx, j)
                
    return [luy, lux, rdy+1, rdx+1]