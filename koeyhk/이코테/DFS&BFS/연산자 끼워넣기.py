import sys
import itertools
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
a, s, m, d = map(int, input().split())

queue = deque()
for i in range(a):      # 연산자 추가하기
    queue.append('+')
for i in range(s):
    queue.append('-')
for i in range(m):
    queue.append('x')
for i in range(d):
    queue.append('/')
perm = list(itertools.permutations(queue, N-1))     # 연산자 순열 생성

ma = -1e9
mi = 1e9
for pe in perm:     # 연산자 순열 내에서
    result = A[0]
    i = 1
    for p in pe:       # 연산자 순서에 따라 연산 진행
        if p == '+':
            result += A[i]
        elif p == '-':
            result -= A[i]
        elif p == 'x':
            result *= A[i]
        else:
            if result*A[i] < 0:     # 둘 중 하나가 음수라면 -1
                a = -1
            else:
                a = 1
            result = abs(result) // abs(A[i])
            result *= a
        i += 1
    ma = max(result, ma)
    mi = min(result, mi)

print(ma)
print(mi)
