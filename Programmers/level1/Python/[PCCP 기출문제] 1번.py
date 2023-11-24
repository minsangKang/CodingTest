# bandage: [시전 시간, 초당 회복량, 추가 회복량]
# attacks: [[공격 시간, 피해량], ...]
# 남은 체력을 return (0 이하가 된다면 -1)
def solution(bandage, health, attacks):
    needTime, plus, bonus = bandage
    hp = health
    t = 0 # 시간
    
    for attackTime, damage in attacks:
        # 체력 회복
        hillTime = (attackTime-1 - t) # 회복가능한 시간
        if hillTime > 0:
            hp = min(health, hp + plus*hillTime) # 체력 plus 반영
            if (hillTime//needTime) >= 1: # 연속 회복 성공시
                hp = min(health, hp + bonus*(hillTime//needTime)) # bonus 반영
        t += hillTime
        
        # attack
        hp -= damage
        t += 1
        
        if hp <= 0:
            return -1
        
    return hp