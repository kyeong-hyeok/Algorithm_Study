import sys

input_data = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input_data().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input_data().split())
    graph[B].append(A)
X = int(input_data())
do = [0] * (N + 1)
visit = [False] * (N+1)


def dfs(v):
    for i in graph[v]:
        if not visit[i]:
            visit[i] = True
            do[v] += dfs(i) + 1
    return do[v]


print(dfs(X))