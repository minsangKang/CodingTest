def count(pattern, answers):
    idx = 0
    count = 0
    for answer in answers:
        if answer == pattern[idx%len(pattern)]:
            count += 1
        idx += 1
    return count

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    count1 = count(pattern1, answers)
    count2 = count(pattern2, answers)
    count3 = count(pattern3, answers)
    maxCount = max(count1, max(count2, count3))
    
    answer = []
    if count1 == maxCount:
        answer.append(1)
    if count2 == maxCount:
        answer.append(2)
    if count3 == maxCount:
        answer.append(3)
    
    return answer