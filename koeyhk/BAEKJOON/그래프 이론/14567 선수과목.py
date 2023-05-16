import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
graph = [[] for _ in range(N + 1)]
prev = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input_data().split())
    graph[a].append(b)
    prev[b] += 1

result = []


def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if prev[i] == 0:
            q.append((i, 1))
    while q:
        a, b = q.popleft()
        result.append((a, b))
        if len(graph[a]) != 0:
            for i in graph[a]:
                prev[i] -= 1
                if prev[i] == 0:
                    q.append((i, b+1))

topology_sort()
result.sort()
for i in result:
    print(i[1], end=' ')