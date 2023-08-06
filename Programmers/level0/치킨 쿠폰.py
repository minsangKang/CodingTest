def solution(chicken):
    coupon = chicken
    count = 0
    while coupon > 9:
        bonus = coupon//10
        count += bonus
        coupon %= 10
        coupon += bonus
    
    return count