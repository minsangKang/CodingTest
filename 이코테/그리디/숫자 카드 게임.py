N, M = map(int, input().split())

cards = []
for i in range(N):
    cards.append(list(map(int, input().split())))

maxCard = -1
for row in range(N):
    maxCard = max(maxCard, min(cards[row]))
print(maxCard)