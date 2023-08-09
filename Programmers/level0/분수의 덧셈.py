import math

def solution(numer1, denom1, numer2, denom2):
    lcm = (denom1*denom2)//math.gcd(denom1, denom2)
    numer1 *= lcm//denom1
    numer2 *= lcm//denom2
    
    numer = numer1+numer2
    gcd = math.gcd(numer, lcm)
    return [numer//gcd, lcm//gcd]