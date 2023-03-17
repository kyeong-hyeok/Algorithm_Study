from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
c = [list(input().split()) for _ in range(N)]
x = []      # 아무것도 존재하지 않는 곳
s = []      # 학생이 존재하는 곳
t = []      # 선생님이 존재하는 곳
for i in range(N):
    for j in range(N):
        if c[i][j] == 'X':
            x.append((i, j))
        elif c[i][j] == 'S':
            s.append((i, j))
        else:
            t.append((i, j))

barrier = list(combinations(x, 3))      # 장애물 3개의 조합
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check(co, x, y, d):   # (복도, (x, y) 좌표, 탐색 방향)
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if co[x][y] == 'O':     # 장애물을 만났을 때
        return 0
    elif co[x][y] == 'S':   # 학생을 만났을 때
        return 1
    nx = x + dx[d]
    ny = y + dy[d]
    if check(co, nx, ny, d):  # 해당 방향으로 탐색 시 학생을 만났다면
        return 1
    return 0


def solution(barrier):
    for b in barrier:   # 장애물 조합 중 하나 택하기
        k = 0       # 학생이 감시에 걸린지 여부
        co = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                co[i][j] = c[i][j]
        for x, y in b:      # 장애물 설치
            co[x][y] = 'O'
        for x, y in t:  # 선생님 위치에서
            for i in range(4):  # 각 방향으로 dfs 수행
                if check(co, x, y, i):    # 학생이 감시에 걸렸다면
                    k = 1
        if k == 0:
            return 1
    return 0


if solution(barrier):
    print("YES")
else:
    print("NO")
