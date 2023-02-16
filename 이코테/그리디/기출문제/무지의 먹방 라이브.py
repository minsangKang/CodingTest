import heapq

def solution(food_times, k):
    # k초가 되기전까지 음식을 다 먹을 수 있는 경우
    if sum(food_times) <= k:
        return -1
    
    # 모든 음식을 시간순으로 정렬해야 한다.
    # 마지막에 음식번호를 출력해야 하기 때문에 heapq(시간, 음식번호) 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    sumTime = 0 # 섭취 누적시간
    removedTime = 0 # 직전에 제거된 음식의 시간
    # 남은 음식의 개수
    foodCount = len(food_times) 
    
    while True :
        now = heapq.heappop(q)
        nowFoodTime = now[0]
        roundTime = foodCount * (nowFoodTime - removedTime)
        # 남은 시간이 해당 음식기준 전체음식을 먹는데 걸리는 시간보다 작은 경우 -> 먹지못하고 종료
        if (k - sumTime) < roundTime:
            heapq.heappush(q, now)
            break;
        # 누적시간 += 현재 음식기준 전체 음식을 먹는데 걸리는 시간
        sumTime += roundTime
        # 남은 음식의 개수 -1
        foodCount -= 1
        # 직전 제거된 음식 반영
        removedTime = nowFoodTime
    
    # 남은 음식들을 음식번호 순으로 정렬한다
    remainFoods = sorted(q, key=lambda x: x[1])
    # 마지막 음식 + 1 위치는 (남은 시간 % 남은 음식개수)
    return remainFoods[(k - sumTime)%foodCount][1]