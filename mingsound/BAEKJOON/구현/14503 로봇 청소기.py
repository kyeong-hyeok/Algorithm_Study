import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
R, C, D = map(int, input().split()) # 처음 위치(R, C), 바라보는 방향 : D
graph = [list(map(int, input().split())) for _ in range(N)] # 청소 X : 0, 벽 : 1

# d 북 동 남 서
#   0  1  2  3
# dx = [1, 0, -1, 0]으로 작성해 헤맸었음...
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 주변 4칸 중에서 청소 안된 칸 있다면 위치 반환
def check(x, y, d):
    for i in range(1, 5):
        nd = (d - i + 4) % 4 # 반시계 방향으로 회전하며 청소 되지 않은 곳 있는지 체크
        nx = x + dx[nd]
        ny = y + dy[nd]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0: # 청소되지 않은 곳 발견
            return nx, ny, nd # 위치, 방향 반환

    return -1, -1, -1 # 4칸 모두 청소되어있다면 -1, -1, -1반환

def bfs():
    queue = deque([(R, C, D)])
    answer = 0

    while True:
        x, y, d = queue.popleft()

        # 현재 칸이 청소되지 않은 경우 청소
        if graph[x][y] == 0:
            graph[x][y] = 2 # 청소했다면 2로 표시
            answer += 1

        nx, ny, nd = check(x, y, d)
        # 현재 칸 주변 4칸 중 청소되지 않은 빈칸 없다면
        if nx == -1:
            nd = d # 방향 유지
            # 후진
            nx = x - dx[nd]
            ny = y - dy[nd]

            # 후진 가능 : 후진
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
                queue.append((nx, ny, nd))
            # 후진 불가 : 중지
            else:
                break

        # 현재 칸 주변 4칸 중 청소되지 않은 빈칸 O
        else:
            # 방향 변경 후, 한칸 전진
                queue.append((nx, ny, nd))
    return answer

print(bfs())
