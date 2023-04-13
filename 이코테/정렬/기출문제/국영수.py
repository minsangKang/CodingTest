import sys
input = sys.stdin.readline

# 국어(내림차순) -> 영어(오름차순) -> 수학(내림차순) -> 이름(오름차순)
n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )

for student in students:
    print(student[0])
