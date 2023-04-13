n = int(input())
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key = lambda x: x[1])
for student in array:
    print(student[0], end=" ")