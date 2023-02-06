move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

inputs = list(input())
row = ord(inputs[0]) - ord('a') + 1
column = int(inputs[1])

count = 0
for m in move:
    nr = row + m[0]
    nc = column + m[1]
    if nr < 1 or nr > 8:
        continue
    if nc < 1 or nc > 8:
        continue
    count += 1
print(count)