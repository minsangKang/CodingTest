def divisors(num):
    arr = [i for i in range(1, int(num**0.5)+1) if num%i == 0]
    arr += [num//i for i in arr]
    return set(arr)

def solution(number, limit, power):
    result = []
    for i in range(1, number+1):
        count = len(divisors(i))
        result.append(count if count <= limit else power)
    
    return sum(result)
    