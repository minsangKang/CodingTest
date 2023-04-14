# 가장 인접한 두 공유기 사이의 거리(gap)의 최댓값
import sys
input = sys.stdin.readline

# 집수, 공유기수
n, c = map(int, input().split())
locations = [int(input()) for _ in range(n)]
locations.sort()

# 파라메트릭 서치: `가장 인접한 두 공유기 사이의 거리(gap)` 값을 조절
# 공유기수가 c와 같다면 -> gap을 높인다 (마지막 gap 값 저장)
# 공유기수가 c보다 많다면 -> gap 을 높인다
# 공유기수가 c보다 적다면 -> gap 을 낮춘다
# 공유기수를 어떻게 계산? -> 설치된 공유기위치 + 현재 gap 보다 크거나 같은 위치의 경우: 공유기 설치 가능위치
def parametricSearch(locations, c, minGap, maxGap):
    # 마지막에 저장된 Gap 값
    lastGap = 0
    
    while minGap <= maxGap:
        # 최소 Gap ~ 최대 Gap 에서 중앙 Gap 값으로 파라메트릭 서치 진행
        mid = (minGap + maxGap) // 2
        # 설치된 공유기 수 (초기값 1: [0])
        count = 1
        # 설치된 공유기 위치값
        baseValue = locations[0]

        # 공유기 설치 진행
        for i in range(1, n):
            if locations[i] >= baseValue + mid:
                baseValue = locations[i]
                count += 1

        # 설치된 공유기수가 c 보다 크거나 같은 경우 -> Gap 을 높인다
        if count >= c:
            lastGap = mid
            minGap = mid + 1
        else:
            maxGap = mid - 1
    
    # 마지막 Gap값 반환
    return lastGap

minGap = 1
maxGap = locations[n-1] - locations[0]

print(parametricSearch(locations, c, minGap, maxGap))