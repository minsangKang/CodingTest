# 떠날 수 있는 그룹 수의 최댓값
n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
