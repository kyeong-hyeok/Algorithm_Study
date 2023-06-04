# 조건 : 익은 것 주변 상하좌우 영향 받아서 익는다
# 구하는 것 : 며칠이지나면 다 익게되는지 최소 일수
# 보통 상하좌우, 모두 다 전파되는데 최소일수 => bfs인듯

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # M : 가로 칸 수, N : 세로 칸 수
# 초기 토마토의 정보
tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 함수
def bfs():
    queue = deque()

    # 초기에 익은 토마토의 (x, y, 익은 일수)를 queue에 저장 & 이미 모든 토마토가 익었다면 0 반환
    checkAlreadyGood = True  # 처음에 안익은 토마토 있는지 확인
    for x in range(N):
        for y in range(M):
            if tomato[x][y] == 1:
                queue.append((x, y, 0))
            if tomato[x][y] == 0:  # 안익은 토마토 있다면
                checkAlreadyGood = False

    if checkAlreadyGood:  # 안익은 토마토가 없다면
        return 0  # 0 반환

    # bfs 수행
    while queue:
        x, y, day = queue.popleft()

        # 상하좌우의 토마토 익게 만들기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 토마토 박스의 범위 안에 있고, 아직 익지 않은 토마토라면(= 아직 방문하지 않았다면)
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                queue.append((nx, ny, day + 1))

    # 안익은 토마토 있는지 확인
    for x in range(N):
        for y in range(M):
            if tomato[x][y] == 0:
                return -1  # 안익은 토마토가 있다면 -1 반환

    # 안익은 토마토가 없는 경우 day값 반환
    return day  # 마지막에 day값이 토마토가 모두 익을 때까지의 최소 날짜 - day값이 클수록 queue의 맨 뒤에 담기니까


print(bfs())

