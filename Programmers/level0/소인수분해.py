def solution(n):
    isPrime = [True]*10001
    for i in range (2, int(n**0.5)+1):
        if isPrime[i] == True:
            for j in range(2*i, n+1, i):
                isPrime[j] = False
                
    primes = [i for i in range(2, n+1) if isPrime[i]]
    return [prime for prime in primes if n%prime == 0]
    