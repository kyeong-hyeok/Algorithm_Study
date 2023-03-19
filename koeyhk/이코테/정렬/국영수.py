import sys

input = sys.stdin.readline

N = int(input())
grade = []
for i in range(N):
    name, k, e, m = input().split()
    grade.append([name, int(k), int(e), int(m)])
grade.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(grade[i][0])