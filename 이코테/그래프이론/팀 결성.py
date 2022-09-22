def find(parents, x):
    if parents[x] !=  x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    parent = min(find(parents, x), find(parents, y))
    parents[x] = parent
    parents[y] = parent

UNION = 0
FIND = 1

N, M = map(int, input().split())
parents = [0]*(N+1)
for i in range(N+1):
    parents[i] = i

for i in range(M):
    func, a, b = map(int, input().split())
    if func == UNION:
        union(parents, a, b)
    else:
        sameParent = find(parents, a) == find(parents, b)
        print("YES" if sameParent else "NO")