import itertools

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    
    return True

def toInt(nums):
    num = 0
    for i in range(len(nums)):
        num += (nums[i]*(10**i))
    return num

def solution(numbers):
    nums = list(map(int, list(numbers)))
    primes = []
    for count in range(1, len(nums)+1):
        npr = itertools.permutations(nums, count)
        for tuple in npr:
            num = toInt(tuple)
            if isPrime(num) and num not in primes:
                primes.append(num)
    print(primes)
    return len(primes)

answer = solution("011")
print(answer)