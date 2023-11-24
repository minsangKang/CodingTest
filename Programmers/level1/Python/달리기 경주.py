# 추월한 선수의 이름: index (swap(index-1, index))
def solution(players, callings):
    dict = { name: idx for idx, name in enumerate(players) }
    for name in callings:
        index = dict[name]
        target = players[index-1]
        
        players[index-1], players[index] = players[index], players[index-1]
        dict[name] = index-1
        dict[target] = index
    
    return players