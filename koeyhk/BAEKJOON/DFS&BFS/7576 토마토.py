import sys
from collections import deque

input_data = sys.stdin.readline

M, N = map(int, input_data().split())
tomato = [list(map(int, input_data().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j, 0))     # x, y 좌표, 날짜
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    if len(q) == N*M:       # 처음부터 모든 토마토가 익어있는 상태라면
        return 0
    while q:
        x, y, d = q.popleft()
        tomato[x][y] = 1
        result = d      # 현재까지의 날짜 저장
        d += 1
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and tomato[xx][yy] == 0:
                    tomato[xx][yy] = 1
                    q.append((xx, yy, d))
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:   # 토마토가 모두 익지 못하는 상황이라면
                return -1
    return result


print(bfs())