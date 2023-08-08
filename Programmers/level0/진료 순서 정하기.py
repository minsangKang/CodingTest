def solution(emergency):
    # index 함수를 이용한 풀이
    return [sorted(emergency)[::-1].index(i)+1 for i in emergency]
    # dictionary 이용한 풀이
    dict = { key: index+1 for index, key in enumerate(sorted(emergency)[::-1]) }
    return [dict[i] for i in emergency]
    