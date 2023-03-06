# 5:05 - 5:30

# 인구 이동이 며칠동안 발생하는지

# idea
# bfs 사용해서 근접 4방면을 아직 방문하지 않았고, 차이가 L이상 R이하라면 방문처리하고 인구수 더해줌
import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().rstrip().split()) # NxN 크기의 땅, 인구 차이가 L이상 R이하인 경우 인구이동가능
graph = [list(map(int, input().rstrip().split())) for _ in range(N)] # 인구 수 배열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인구 이동 수행
def bfs(visited, x, y):
    position = [(x, y)] # 연합 위치들 리스트
    total = graph[x][y] # 연합의 총 인구 수

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 근접 4방향 검사
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: # 범위 안에 있고, 아직 방문하지 않았다면
                diff = abs(graph[x][y] - graph[nx][ny]) # 인구 차
                if L <= diff <= R: # 인구 차가 L이상 R이하라면
                    visited[nx][ny] = True # 방문처리
                    total += graph[nx][ny] # 전체 인구수에 값 추가
                    queue.append((nx, ny)) # 큐에 위치 추가
                    position.append((nx, ny)) # 연합 리스트에 추가

    ppl = total // len(position)
    for x, y in position: # 연합들의 인구 값 수정
        graph[x][y] = ppl

# 인구이동이 더이상 발생하지 않는지 체크
def check():
    for x in range(N):
        for y in range(N):
            for k in range(4): # 근접 4방향 검사
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N: # 범위 안에 있으면서
                    if L <= abs(graph[x][y] - graph[nx][ny]) <= R: # 인구 차가 L이상 R이하인 경우가 있다면
                        return False # 아직 인구이동이 더 발생할 수 있고 False 반환

    return True

day = 0 # 인구이동 며칠동안 이뤄지는지
while True:
    if check(): # 인구이동 더 이상 발생하지 않는다면
        break

    day += 1

    visited = [[False] * N for _ in range(N)]

    for i in range(N): # 모든 위치에 대해서
        for j in range(N):
            if not visited[i][j]: # 아직 방문하지 않은 곳이 있다면 인구이동 수행
                bfs(visited, i, j)

print(day)