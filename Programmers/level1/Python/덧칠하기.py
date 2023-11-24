def solution(n, m, section):
    count = 1
    start = section[0]
    
    for s in section:
        end = start+m-1
        
        if s <= end:
            continue
        else:
            count += 1
            start = s
            
    return count