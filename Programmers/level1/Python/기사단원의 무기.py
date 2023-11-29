# 약수구하기 (제곱근까지 확인, 약수로 나눈 값까지)
def divisors(num):
    arr = [i for i in range(1, int(num**0.5)+1) if num%i == 0]
    arr += [num//i for i in arr]
    return set(arr)

def solution(number, limit, power):
    result = []
    for i in range(1, number+1):
        divisorsCount = len(divisors(i))
        result.append(divisorsCount if divisorsCount <= limit else power)
    return sum(result)