N = int(input())
students = []
for i in range(N):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda x : x[1])
for s in students:
    print(s[0], end=" ")
print()