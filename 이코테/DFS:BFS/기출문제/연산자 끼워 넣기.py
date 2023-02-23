# 만들 수 있는 식의 결과값의 최댓값, 최솟값을 출력
from itertools import permutations
import math
PLUS, MINUS, MULTI, DIVID = 0, 1, 2, 3

n = int(input())
num = list(map(int, input().split()))
plus, minus, multi, divid = map(int, input().split())

operations = []
operations.extend([PLUS]*plus)
operations.extend([MINUS]*minus)
operations.extend([MULTI]*multi)
operations.extend([DIVID]*divid)

maxValue = -math.inf
minValue = math.inf

for oper in permutations(operations, n-1):
    result = num[0]
    for i in range(1, n):
        if oper[i-1] == PLUS:
            result += num[i]
        elif oper[i-1] == MINUS:
            result -= num[i]
        elif oper[i-1] == MULTI:
            result *= num[i]
        elif oper[i-1] == DIVID:
            result = int(result/num[i])
    
    maxValue = max(maxValue, result)
    minValue = min(minValue, result)

print(maxValue)
print(minValue)