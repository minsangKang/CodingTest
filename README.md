# CodingTest

## [코딩테스트 정리 노션](https://deeply-eggplant-5ec.notion.site/fc62882281f84f06af00aa5ad3bc56ec)

---

# 파이썬 라이브러리

## itertools

permutation

## collections

deque(queue)

## sys

sys.stdin.readline().rstrip()

```python
import sys

input_data = sys.stdin.readline().rstrip()
```

## Sort

```python
arr = [1,2,3]
sorted_arr = sorted(arr)

arr.sort()

data = [("바나나", 2), ("당근", 3)]
data.sort(key=lambda x : (x[0], x[1]))
```

# 파이썬 자료구조

## Stack

```python
stack = []
stack.append(5)
stack.pop()

print(stack) # 최하단부터
print(stack[::-1]) # 최상단부터
```

## Queue

```python
from collections import deque

queue = deque()
queue.append(5)
queue.popleft()

print(queue) # 들어온 순
queue.reverse()
print(queue) # 역순
```

---

# 그리디

가장 큰 순서대로, 가장 작은 순서대로 와 같은 기준

정렬 알고리즘과 짝을 이룬다.

큰 단위가 작은 단위의 배수형태여야 한다. 아닌 경우 다이나믹 프로그래밍으로 접근

# 구현

완전탐색

시뮬레이션

# 그래프

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

# DFS/BFS

스택, 큐

재귀: 스택구조, 종료 조건이 필요

DFS: 스택(재귀)

- 방문하지 않은 경우 재귀를 통해 새로운 노드 방문

```python
def dfs(graph, v, visited):
	visited[v] = True

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
```

BFS: 큐

- 방문하지 않은 경우 queue 에 추가, queue 순서에 맞게 노드 방문

```python
def bfs(graph, start, visited):
	queue = dequeue([start])
	visited[start] = True

	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
```

# 선택 정렬

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

# 삽입 정렬

`O(n^2)` but 데이터가 거의 정렬되어 있을 때 효율적

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

# 퀵 정렬

`O(n log n)` but 데이터가 거의 정렬되어 있을 때 비효율적

pivot 을 기준으로 작은, 큰 데이터 좌우 분리, 분리된 좌, 우 역시 동일 방식으로 정렬

좌 → 우: pivot 보다 큰 데이터, 좌 ← 우: pivot 보다 작은 데이터를 찾아 위치를 서로 변경

작은 데이터 위치가 큰 데이터 위치보다 작은 경우: pivot, 작은 데이터 switch, 종료

재귀 종료조건: 리스트가 1개인 경우 정렬된 상태이므로 반환

pivot 선택기준: 첫번째 데이터 (호어 분할 방식)

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

# 계수 정렬

`O(n + k)` (k: 가장큰 수)

범위가 정해진 정수, 중복이 많은 경우 효율적

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

# 병합 정렬

`O(n log n)` 퀵정렬보다는 느리지만 최악의 경우도 보장

# 순차 탐색

`O(n)`

앞에서부터 차례로 확인

```python
def search(array, target):
	for i in range(len(array)):
		if array[i] == target:
			return i
	return -1
```

# 이진 탐색

`O(log n)`

정렬된 배열 내에서 중간점 위치 데이터와 비교하며 반복적으로 절반씩 좁혀가며 찾는다

- 재귀 스타일

```python
def search(array, target):
	return binary_search(array, target, 0, len(array)-1)

def binary_search(array, target, start, end):
	if start > end:
		return -1

	mid = (start + end) // 2
	if array[mid] == target:
		return mid
	elif target < array[mid]:
		return binary_search(array, target, start, mid-1)
	else:
		return binary_search(array, target, mid+1, end)
```

- 반복문 스타일

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

# 이진 탐색 트리

이진 탐색이 동작할 수 있도록 고안된 트리 자료구조

child-left < parent < child-right 식

# 다이나믹 프로그래밍

---

# 에라토스테네스 체

# 메모이제이션

# 플로이드 워셜

# 다익스트라

# GCD
