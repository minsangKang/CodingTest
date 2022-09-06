xPos = ["a", "b", "c", "d", "e", "f", "g", "h"]
move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

input = list((input()))
x = xPos.index(input[0])+1
y = int(input[1])

count = 0
for direction in move:
    nextX = x + direction[0]
    nextY = y + direction[1]

    if nextX >= 1 and nextX <= 8 and nextY >= 1 and nextY <= 8:
        count += 1

print(count)


