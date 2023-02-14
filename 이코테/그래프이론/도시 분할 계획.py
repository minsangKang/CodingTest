import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a-1, b-1))
    
edges.sort()

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
    
result = 0
maxCost = 0
for edge in edges:
    cost, a, b = edge
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        union_parent(a, b)
        result += cost
        maxCost = cost
        
print(result - maxCost)