def solution(today, terms, privacies):
    # 오늘 날짜로 파기해야 할 개인정보 번호들 반환
    dict = { t.split()[0]: int(t.split()[1]) for t in terms }
    ty, tm, td = map(int, today.split('.'))
    
    result = []
    for index, p in enumerate(privacies):
        pday, pt = p.split()
        py, pm, pd = map(int, pday.split('.'))
        # 계약에 따라 날짜 계산
        pm += dict[pt]
        py += (pm-1)//12
        pm = pm%12 or 12
        # today 와 py, pm, pd 비교
        if ty*10000+tm*100+td >= py*10000+pm*100+pd:
            result.append(index+1)
    
    return result