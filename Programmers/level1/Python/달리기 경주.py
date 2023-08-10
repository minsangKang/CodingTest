def solution(players, callings):
    # call -> index가 O(1)이 되어야 함
    # 그리고 index -> name또한 가능해야 함
    # dictionary로 call -> index를 하고
    # index -> name은 배열로 관리
    dict = { name: index for index, name in enumerate(players) }
    for call in callings:
        index = dict[call]
        dict[call] -= 1
        dict[players[index-1]] += 1
        players[index-1], players[index] = players[index], players[index-1]
    return players