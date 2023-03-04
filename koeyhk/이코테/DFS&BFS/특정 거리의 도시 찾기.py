import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
road = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    road[a].append(b)
visit = [-1] * (N + 1)  # visit를 0으로 초기화 하면 시작점을 재방문하게 됨


def bfs(x, k):
    queue = deque()
    queue.append(x)
    result = []
    visit[x] = 0  # 시작점 방문
    while queue:
        v = queue.popleft()
        for r in road[v]:
            if visit[r] == -1:
                visit[r] = visit[v] + 1
                queue.append(r)
                if visit[r] == k:
                    result.append(r)
    return result


result = bfs(X, K)
result.sort()
if len(result):
    for r in result:
        print(r)
else:
    print(-1)
