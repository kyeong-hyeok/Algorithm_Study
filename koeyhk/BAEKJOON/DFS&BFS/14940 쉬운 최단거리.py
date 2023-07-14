import sys
from collections import deque

input_data = sys.stdin.readline

n, m = map(int, input_data().split())
land = [list(map(int, input_data().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
length = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if land[nx][ny] != 0 and visited[nx][ny] == 0:
                    length[nx][ny] = length[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return True


for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            bfs(i, j)
            break
for i in range(n):
    for j in range(m):
        if land[i][j] == 1 and length[i][j] == 0:
            print(-1, end=' ')
        else:
            print(length[i][j], end=' ')
    print()
