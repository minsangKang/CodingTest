def solution(babbling):
    s = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for bab in babbling:
        for b in s:
            if b in bab and b+b not in bab:
                bab = bab.replace(b, ' ')
        bab = bab.replace(' ', '')
        if len(bab) == 0:
            count += 1
        
    return count