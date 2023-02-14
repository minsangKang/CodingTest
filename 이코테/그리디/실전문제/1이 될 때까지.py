n, k = map(int, input().split())
count = 0

while True:
    canDiv = k * (n // k) #k 배수
    count += (n - canDiv) #1 빼기: 한번에 연산
    n = canDiv
    
    if n < k:
        break
    n //= k #k로 나누기
    count += 1

print(count)