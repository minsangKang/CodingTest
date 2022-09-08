def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

v, e = map(int, input().split())
parents = [0]*(v+1)

for i in range(1, v+1):
    parents[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parents, a) == find_parent(parents, b):
        cycle = True
        break
    else:
        union_parent(parents, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 비발생")