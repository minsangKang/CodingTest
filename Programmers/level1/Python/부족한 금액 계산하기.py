def solution(price, money, count):
    return max(0, price*(count*(count+1)/2) - money)