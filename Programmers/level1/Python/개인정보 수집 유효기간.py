def solution(today, terms, privacies):
    dict = {}
    for t in terms:
        key, value = t.split()
        dict[key] = int(value)
    
    result = []
    ty, tm, td = map(int, today.split("."))
    today = ty*10000+tm*100+td
    
    for idx, privacy in enumerate(privacies):
        pdate, case = privacy.split()
        py, pm, pd = map(int, pdate.split("."))
    
        pm += dict[case]
        py += (pm-1)//12
        pm = pm%12 or 12
        
        if py*10000+pm*100+pd <= today:
            result.append(idx+1)
    return result