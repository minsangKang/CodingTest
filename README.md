# CodingTest with Python
[Python 문법 및 알고리즘 정리 블로그링크](https://velog.io/@minsang/series/Python)

---

# 파이썬 라이브러리
## itertools (순열, 조합) ⭐️⭐️
```python
# 순열
from itertools import permutation

for case in permutations(array, len(array)):
    ...
```
```python
# 조합
from itertools import combinations

for case in combinations(array, len(array)):
    ...
```

## functools (reduce)
```python
# reduce
from functools import reduce

result = reduce(lambda x, y: x*y, array)
```

## collections (deque(queue)) ⭐️
```python
from collections import deque

queue = deque() # queue 생성
queue.append('a') # push
queue[0] # peak 'a'
queue.popleft() # pop 'a'
queue.extend(['b', 'c', 'd']) # 배열 push
```

## heapq (priorityQueue) ⭐️
```python
import heapq

pq = [] # priorityQueue 생성
heapq.heappush(pq, (0, 1)) # push
pq[0] # peak (0, 1)
heapq.heappop(pq) # pop (0, 1)

array = [b, c, a]
heapq.heapify(array) # array를 priorityQueue로 생성
heapq.heappop(array) # pop 'a'
```

## math (gcd)
```python
import math

value = math.gcd(3, 6)
```

## copy
```python
import copy

array2 = copy.deepcopy(array)
```

## sys (readline)
```python
import sys

input = sys.stdin.readline()
```

---

# Python 기본 자료구조

## Stack
```python
stack = [] # stack 생성
stack.append('a') # push
stack[0] # peak
stack.pop() # pop 'a'
```

## Set
```python
s = set() # set 생성
s1 = set(['a', 'b', 'c']) # array를 set으로 생성
s2 = set(['b', 'c', 'd'])

s1 & s2 # 교집합 {'b', 'c'}
s1 | s2 # 합집합 {'a', 'b', 'c', 'd'}
s1 - s2 # 교집합을 제거한 s1 {'a'}

{ x for x in 'abcde' } # list comprehension {'a', 'b', 'c', 'd', 'e'}

'a' in s1 # True

list(s1) # set to list ['a', 'b', 'c']
```

## Dictionary
```python
d = {} # dictionary 생성
d = {'a': 1, 'b': 2}
d = dict([('a', 1), ('b', 2)]) # touble array로 생성
d_from_list = { x: ord(x) for x in 'abc' } # list comprehension {'a': 97, 'b': 98, 'c': 99}

d['a'] # value 접근 1
d['a'] = 3 # value update
del d['a'] # value delete

'a' in d # True
list(d) # ['a', 'b']

d.items(): # [(key, value)] 반환 [('b': 2)]
d.keys() # ['b']
d.values() # [2]

for key, value in items(): # key, value 순차접근
    print(key, value)
```

## List
```python
array = [] # list 생성
array.append('a') # push
array.remove('a') # delete
array = list(range(0, 5)) # [0, 1, 2, 3, 4]
array.index(3) # index 3
array.count(3) # 1

array[-1] # 4
array[:-1] # return [0, 1, 2, 3]
array[1:-1] # return [1, 2, 3]
array[::2] # return [0, 2, 4]
array[-1::-2] # return [4, 2, 0]
array[1:-1][::-1] # return [3, 2, 1]

temp = array + [5, 6] # return [1, 2, 3, 4, 5, 6]
array += [5, 6] # update [1, 2, 3, 4, 5, 6]
```

## Tuple
```python
tuple = ('a', 1) # tuple 생성
tuple[0] # 'a'
tuple[1] # 1
```

## String
```python
str(1) # '1'
str(1)+str(2) # '12'
string = 'abc'
string.swapcase() # return 'ABC'
string.isupper() # return False
string.islower() # return True
string.upper() # return 'ABC'
string.lower() # return 'abc'

string = '123'
string.isdecimal() # return True

string = ' abcd '
string.strip() # return 'abcd'
```

## range
```python
list(range(0, 5)) # [0, 1, 2, 3, 4]
for i in range(0, 5):
    print(i, end=", ") # 0, 1, 2, 3, 4,
```

---

# 파이썬 기능들

## sort
```python
# list.sort()
array = [1, 4, 5, 2, 3]
array.sort() # update [1, 2, 3, 4, 5]
array.sort(key=lambda x: -x) # update [5, 4, 3, 2, 1]
array.sort(key=lambda x: abs(x-3)) # update [3, 4, 2, 5, 1]
array.sort(reverse=True) # update [5, 4, 3, 2, 1]
```

## sorted
```python
# sorted(array)
array = [1, 4, 5, 2, 3]
sorted(array) # return [1, 2, 3, 4, 5]
sorted(array, key=lambda x: -x) # return [5, 4, 3, 2, 1]
sorted(array, reverse=True) # return [5, 4, 3, 2, 1]

sorted({1: 'a', 2: 'b'}) # dictionary: return [1, 2]
sorted([('a', 3, 10), ('b', 1, 9), ('c', 2, 9)], key=lambda x: (x[2], x[1])) # tuple: return [('b', 1, 9), ('c', 2, 9), ('a', 3, 10)]
```

## filter
```python
array = [1, 2, 3, 4, 5]
list(filter(lambda x: x>2, array)) # [3, 4, 5]
```

## enumerate
```python
array [1, 2, 3]
for idx, value in enumerate(array):
    print(idx, value, end=",") # 0 1,1 2,2 3,
```

```python
total = sum([1, 2, 3]) # 6
array = sum([[1, 2], [3, 4]], []) # [1, 2, 3, 4]
```

## join
```python
# string.join()
''.join(['a', 'b', 'c']) # return 'abc'
```

## replace
```python
# string.replace()
'abcde'.replace('a', 'A') # return 'Abcde'
```

## ord
```python
counts = [0]*26
for char in 'abcde':
    counts[ord(char)-ord('a')] += 1
```

## map
```python
a, b = map(int, input().split())
```

## Infinity
```python
INF = int(1e9)
```

## abs
```python
abs(-4) # 4
```

# 3항연산자
```python
num = 5
odd = True if num%2 == 1 else False # True
```

---

# 코딩테스트 알고리즘

## 그리디
가장 큰 순서대로, 가장 작은 순서대로 와 같은 기준 (정렬 알고리즘과 한쌍) <br>
큰 단위가 작은 단위의 배수형태여야 한다. 아닌 경우 다이나믹 프로그래밍으로 접근

+ while문 대신 몫을 계산하는 식으로 접근

## 구현 ⭐️
완전탐색 or 시뮬레이션
```python
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ny, nx = y+move[direction][0], x+move[direction][1]
if ny < 0 or ny >= n or nx < 0 or nx >= n:
    direction = (direction+1)%4
    y, x = y+move[direction][0], x+move[direction][1]
```
```python
dict = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}

nx, ny = x+dict[key][0], y+dict[key][1]
if nx < -n or nx > n:
```

## 그래프
노드와 노드 사이에 연결된 간선 정보를 가지고 있는 자료구조

인접행렬
```python
n, m = map(int, input().split())
graph = []
for row in range(n):
    line = [int(x) for x in list(input())]
    graph.append(line)
```

인접 리스트
```python
n, m = map(int, input().split())
graph = [[] for i in range(n)]
graph[0].append((1, 7)) #노드 1, cost 7
graph[1].append((0, 7)) #노드 0, cost 7
```

## DFS/BFS
스택, 큐(deque: from collections) 자료구조 필요 <br>
재귀: 스택구조, 종료 조건이 필요<br>

DFS: 스택(재귀)<br>
- 방문하지 않은 경우 재귀를 통해 새로운 노드 방문
```python
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

BFS: 큐(deque)
- 방문하지 않은 경우 queue 에 추가, queue 순서에 맞게 노드 방문
```python
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

## 선택 정렬
`O(n^2)`
```python
def sort(array):
    for i in range(len(array)):
        min_index = i;
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j;
        array[i], array[min_index] = array[min_index], array[i]
    return array
```

## 삽입 정렬
`O(n^2)` but 데이터가 거의 정렬되어 있을 때 효율적<br>
정렬된 상태 + 적절한 위치 찾아 삽입하여 정렬
```python
def sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # i to 1 까지  -1씩 감소
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array
```

## 퀵 정렬
`O(n log n)` but 데이터가 거의 정렬되어 있을 때 비효율적<br>
`pivot` 을 기준으로 `작은`, `큰` 데이터 좌우 분리, 분리된 좌, 우 역시 동일 방식으로 정렬<br>

좌 → 우: pivot 보다 큰 데이터, 좌 ← 우: pivot 보다 작은 데이터를 찾아 위치를 서로 변경<br>
작은 데이터 위치가 큰 데이터 위치보다 작은 경우: pivot, 작은 데이터 switch, 종료<br>

재귀 종료조건: 리스트가 1개인 경우 정렬된 상태이므로 반환<br>
pivot 선택기준: 첫번째 데이터 (호어 분할 방식)<br>
```python
def sort(array):
    quick_sort(array, 0, len(array)-1)

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1 # find 큰값 index
        while right > start and array[right] >= aray[pivot]:
            right -= 1 # find 작은값 index

        if left > right: # 엇갈린 경우: pivot, 작은값 switch
            array[right], array[pivot] = array[pivot], array[right]
            pivot = right
        else: # 큰값, 작은값 switch, 이후 while 통해 다음 switch 진행
            array[left], array[right] = array[right], array[left]
    # pivot 보다 작은 값들 | pivot | pivot 보다 큰 값들
    quick_sort(array, start, pivot-1)
    quick_sort(array, pivot+1, end)
```
```python
def sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return sort(left_side) + [pivot] + sort(right_side)
```

## 계수 정렬
`O(n + k)` (k: 가장큰 수)<Br>
범위가 정해진 정수, 중복이 많은 경우 효율적<br>
위치변경 X, 리스트 정보를 통한 정렬
```python
def sort(array):
  counts = [0]*(max(array)+1)
  
  for i in range(len(array)):
        counts[array[i]] += 1

  sorted = []
  for i in range(len(counts)):
        sorted += [i] * counts[i]

  return sorted
```

## 병합 정렬
`O(n log n)` 퀵정렬보다는 느리지만 최악의 경우도 보장<br>

## 순차 탐색
`O(n)` 앞에서부터 차례로 확인<br>
```python
def search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
```

## 이진 탐색 ⭐️
`O(log n)` 정렬된 배열 내에서 중간점 위치 데이터와 비교하며 반복적으로 절반씩 좁혀가며 찾는다<br>
재귀 형식과 반복문 형식이 있는데, stack에 쌓이지 않는 반복문 방식이 더 좋다.
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1
```

## 파라메트릭 서치 (Parametric Search)
주어진 범위 내에서 원하는 값 또는 원하는 조건에 가장 일치하는 값을 찾아내는 알고리즘<br>
최적화 문제(최댓값 x = ?) -> 결정문제(x일 경우 최댓값?)로 바꾸어 풀 수 있다.<br>
- 범위의 중간값과 조건을 비교하며 범위를 수정해나간다
- 이진 탐색과 차이점은 값 비교 -> 조건 비교, 반환값 (mid, -1 -> result (현재까지의 최적값))이 다르다는 점.
```python
# 최적화문제: 24시간을 7시간마다 배고파지는 사람이 최소 몇끼니를 먹어야 배부르게 지낼수있는가?
# 결정문제: 7시간마다 배고파지는 사람이 x끼니를 먹으면 24시간을 배부르게 지낼 수 있다.
def parametricSearch(start, end) {
    mid = (start + end) / 2
    currentValue = mid
    while (start <= end):
        if (24 / mid) > 7:   
            start = mid + 0.1
        elif (24 / mid) < 7:
            end = mid - 0.1
        else
            return currentValue
    return mid
}
```
[파라메트릭 서치 블로그](https://marades.tistory.com/7)

## 이진 탐색 트리
이진 탐색이 동작할 수 있도록 고안된 트리 자료구조<br>
child-left < parent < child-right 식

## 다이나믹 프로그래밍
큰 문제를 작은 문제로 나눌 수 있는 경우 동일문제를 중복되지 않게 계산하는 방법<br>
Bottom up(반복문), Top down(재귀) 방식<br>
메모이제이션: 계산된 결과들을 메모하는 기법 (캐싱)<br>
`O(n)`
```python
d = [0] * 100
def pibo(x):
    d[1] = 1
    d[2] = 1
    
    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]
```

## 다익스트라
시작 노드로부터 각 노드까지의 최단거리 알고리즘 (음의 간선이 없는 경우)<br>
반복적으로 최소 최단거리의 노드를 선택하며 테이블을 갱신 (heapq 사용)<br>
`O(E log V)`
- `V`: 노드수, `E`: 간선수
- `visited`: [False] * (n+1)
- `distance`: [INF] * (n+1)
```python
def dijkstra(graph, startNode):
    distance = [INF]*(len(graph)+1)
    distance[startNode] = 0
    q = []
    # q: (distance, node), distance 가 적은 node 순으로 정렬된다
    heapq.heappush(q, (0, startNode))
    
    while q:
        currentDistance, currentNode = heapq.heappop(q)
        # currentNode 의 distance 가 갱신된적이 있는 경우 무시
        if distance[currentNode] < currentDistance:
            continue
        
        # currentNode 의 인접노드들 확인
        for node in graph[currentNode]:
            nodeNum = node[0]
            nodeCost = node[1]
            newDistance = currentDistance + nodeCost

            if newDistance < distance[nodeNum]:
                distance[nodeNum] = newDistance
                heapq.heappush(q, (newDistance, nodeNum))
                    
    return distance
```
```python
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
startNode = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    from, to, cost = map(int, input().split())
    graph[from].append((to, cost))

distance = dijkstra(graph, startNode)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```

## 플로이드 워셜
여러개의 from, to 노드간 최단거리 구하기 알고리즘<br>
점화식: `AtoB = min(AtoB, AtoK + KtoB)`<br>
k, a, b 순차적으로 3중 for 구조<br>
`O(n^3)`
```python
def floydWarshall(graph):
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                graph[b][a] = graph[a][b]
```
```python
import sys
input = sys.stdin.readline()
INF = int(1e9)

n, m = map(int, input().split())
graph = [[]]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            graph[b][a] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost

floydWarshall(graph)

for a in range(1, n+1):
    for b in range(1, n+1):
        val = graph[a][b] if graph[a][b] != INF else "INF"
        print(val, end=" ")
    print()
```

## 서로소 집합
공통 원소가 없는 집합이 필요한 경우<br>
하나의 집합으로 합치는 `union` 과 원소가 속한 집합을 알려주는 `find` 연산이 필요<br>
`union` 의 경우 `작은 노드값`이 집합의 값이 된다.<br>
```python
# 노드값과 집합값이 같을때까지 재귀적으로 호출
def findParent(parents, x):
    if parents[x] != x:
        parents[x] = findParent(parents, parants[x])
    return parents[x]

def unionParent(parents, a, b):
    setA = findParent(parents, a)
    setB = findParent(parents, b)
    
    if setA < setB:
        parents[b] = setA
    else:
        parents[a] = setB
```
```python
v, e = map(int, input().split())
parents = [i for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    unionParent(parents, a, b)
    
for i in range(1, v+1):
    print(findParent(parents, i), end=" ")
print()
```

## 사이클 판별
`유향` 그래프: `DFS` 알고리즘<br>
`무향` 그래프: `서로소` 집합 알고리즘<br>
```python
# 무향그래프에서 사이클 판별
v, e = map(int, input().split())
parents = [i for i in range(v+1)]

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    
    if findParent(parents, a) == findParent(parents, b):
        cycle = True
        break
    else:
        unionParent(parents, a, b)
        
if cycle:
    print("사이클 발생")
else:
    print("사이클 비발생")
```

## 신장 트리
모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프<br>
모든 도시를 연결할 때 최소 비용과 관련된 크루스칼 알고리즘의 경우 최소 신장 트리를 활용한 알고리즘<br>

최소 신장 트리를 구하기 위한 알고리즘
- `신장 트리(Spanning tree)`: 모든 정점을 포함, 정점간 서로 연결, 싸이클이 존재하지 않는 그래프
- `최소 신장 트리(Minimum Spanning Tree)`: 신장 트리 중 가중치 합이 최소인 그래프
- 싸이클 여부: `서로소 집합(Disjoint Set)`의 `Union & Find` 활용
[크루스칼 알고리즘 블로그](https://chanhuiseok.github.io/posts/algo-33/)

## 크루스칼 알고리즘
경로를 최소한의 비용으로 연결하는 알고리즘<br>
그래프 내 모든 정점들을 가장 적은 비용으로 연결하기 위해 사용 (사이클이 없는, 가중치의 합 최소가 되는 상태)<br>
모든 간선에 대해 비용값 기준 정렬, 사이클이 발생하지 않는 간선부터 집합에 포함<br>
무향 그래프이므로 find, union 을 통해 사이클 여부 판별 후 간선비용 총합<br>
`O(E log E)`
```python
v, e = map(int, input().split())
parents = [i for i in range(v+1)]
edges = [(a, b, cost) for _ in range(e) a, b, cost = map(int, iniput().split())]
result = 0

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if findParent(parents, a) != findParent(parents, b):
        unionParent(parents, a, b)
        result += cost

print(result)
```

## 위상정렬
우선순위(선후관계)에 따라 방향성에 거스르지 않도록 순서대로 나열<br>
진입차수 테이블과 deque가 필요<br>
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌때까지 꺼내며 해당 노드부터 출발하는 간선을 제거하며 진입차수가 0인 노드를 큐에 넣는다
`O(V+E)`
```python
def topologySort(graph, indegree):
    result = []
    q = deque()
    
    # 처음 시작시 indegree 값이 0인 노드를 넣고 시작
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        node = q.popleft()
        result.append(node)
        
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    return result
```
```python
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
sorted = topologySort(graph, indegree)

for n in result:
    print(n, end=" ")
```

## 소수 알고리즘
2부터 n-1까지 나누어 떨어지는 수가 없는 경우 소수 판별
```python
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
```

## 에라토스테네스의 체
정해진 범위 내 소수를 구하는 경우 사용되는 알고리즘<br>
범위 내 숫자들에서 합성수를 반복적으로 지우는 방식으로 소수를 찾는다.<br>
- 지워지지 않은수 중 작은수를 소수로 채택, 해당 수의 배수를 모두 제거
```python
import math

def prime_list(n):
    prime = [True]*(n+1)
    
    for i in range(2, math.isqrt(n)+1):
        if prime[i] == True:
            for j in range(2*i, n+1, i):
                prime[j] = False
                
    return [i for i in range(2, n+1) if prime[i] == True]
```
[에라토스테네스의 체 블로그1](https://wikidocs.net/21638)
[에라토스테네스의 체 블로그2](https://this-programmer.tistory.com/409)