def solution(numLog):
    dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ''
    for i in range(len(numLog)-1):
        term = numLog[i+1]-numLog[i]
        answer += dict[term]
    return answer