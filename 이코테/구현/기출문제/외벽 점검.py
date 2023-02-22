from itertools import permutations
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값을 반환
def solution(n, weak, dist):
    # 취약 지점 개수
    weakSize = len(weak)
    # 원형을 길이 2배로 늘린 일자형태로 변형
    weak = weak + [w + n for w in weak]
    # 투입할 친구수 초기값은 친구수+1
    minCount = len(dist) + 1
    # 취약지점 시작점
    for weakStart in range(weakSize):
        # 친구들 순서나열
        for friends in permutations(dist, len(dist)):
            # 투입할 친구수
            count = 1
            # 점검할 수 있는 마지막 위치 = 취약지점 + 가능길이
            endPoint = weak[weakStart] + friends[count-1]
            
            # 취약지점을 돌면서 확인
            for i in range(0, weakSize):
                index = weakStart + i
                # 범위를 벗어난 경우
                if weak[index] > endPoint:
                    # 새로운 친구 투입
                    count += 1
                    # 더 투입이 불가한 경우 종료
                    if count > len(dist):
                        break
                        
                    # 점검할 수 있는 마지막 위치 = 현재 취약지점 + 가능 길이 업데이트
                    endPoint = weak[index] + friends[count-1]
            
            # 원을 전부 확인한 경우 최소값 업데이트        
            minCount = min(minCount, count)
    # 모든 친구 투입에도 불가한 경우
    if minCount > len(dist):
        return -1
    
    return minCount