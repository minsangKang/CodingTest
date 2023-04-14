n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    unionCheck, a, b = map(int, input().split())
    if unionCheck == 1:
        a = find_parent(a)
        b = find_parent(b)
        print("YES" if a == b else "NO")
    else:
        union_parent(a, b)