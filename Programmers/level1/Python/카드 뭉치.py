def solution(cards1, cards2, goal):
    left_idx, right_idx = 0, 0
    
    for target in goal:
        if left_idx < len(cards1) and target == cards1[left_idx]:
            left_idx += 1
            continue
        if right_idx < len(cards2) and target == cards2[right_idx]:
            right_idx += 1
            continue
        return "No"
        
    return "Yes"