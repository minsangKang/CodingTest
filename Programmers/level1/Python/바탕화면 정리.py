def solution(wallpaper):
    # 최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일들을 선택
    # return [좌상단 파일 위치, 우하단 파일위치+(1, 1)위치]
    LeftY, LeftX, RightY, RightX = len(wallpaper), len(wallpaper[0]), 0, 0
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                LeftY, LeftX = min(LeftY, y), min(LeftX, x)
                RightY, RightX = max(RightY, y), max(RightX, x)
    return [LeftY, LeftX, RightY+1, RightX+1]
                