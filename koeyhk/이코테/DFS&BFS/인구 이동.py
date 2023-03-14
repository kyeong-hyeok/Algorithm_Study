import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    union = [(x, y)]  # 연합
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상 하 좌 우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(P[x][y] - P[nx][ny]) <= R and not visit[nx][ny]:
                visit[nx][ny] = 1
                union.append((nx, ny))  # 연합에 추가
                queue.append((nx, ny))  # 큐에 추가
    return union


day = 0  # 인구 이동 기간
while 1:
    move = 0       # 인구 이동 여부
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:     # 방문하지 않았을 경우
                union = bfs(i, j)
                if len(union) != 1:     # 연합이 있을 경우
                    move = 1
                    population = 0  # 연합의 인구 수
                    for x, y in union:
                        population += P[x][y]
                    population //= len(union)   # 연합을 이루고 있는 각 칸의 인구수
                    for x, y in union:
                        P[x][y] = population
    if not move:
        print(day)
        break
    day += 1

# bfs에서 반환해야 하는 값을 생각해보기!
# **union**