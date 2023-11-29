# 받은 콜라, 마시는 의미를 둔 코드
def solution(a, b, n):
    emptyBottle = n
    more = 0
    bottle = 0
    while emptyBottle >= a:
        ssang = emptyBottle//a
        emptyBottle -= ssang*a
        bonusBottle = ssang*b
        more += bonusBottle
        # 받은 콜라를 그대로 마신다
        emptyBottle += bonusBottle
        
    return more