import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union(i+1, j+1)

checklist = list(map(int, input().split()))

parent = find(checklist[0])
cant = False
for i in range(1, m):
    if find(i) != parent:
        cant = True
        break

print("NO" if cant else "YES")