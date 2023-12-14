# 약수구하는 함수 방법
def solution(left, right):
    result = 0
    for n in range(left, right+1):
        nums = divisors(n)
        if len(nums)%2 == 0:
            result += n
        else:
            result -= n
            
    return result
    
def divisors(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            result.append(i)
            result.append(n/i)
    return set(result)

# 제곱근이 자연수인 경우(제곱수인 경우)는 약수가 홀수
def solution(left, right):
    result = 0
    for n in range(left, right+1):
        if int(n**0.5) == n**0.5:
            result -= n
        else:
            result += n
            
    return result