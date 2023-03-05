# 10:01 - 10:33

# 0: 빈칸, 1: 벽, 2: 바이러스
# 무조건 벽 3개를 세워서 바이러스를 막으려고 한다.
# 안전 영역 : 벽 3개 세운뒤 바이러스가 퍼질 수 없는 곳
# 안전 영역 크기의 최댓값을 구해라

# idea
# (64 C 3) * 64 = (64 * 63 * 62 * 64) / (3 * 2) = 대략 200만
# 벽 3개 세울 수 있는 모든 경우의 수에 대해서 안전 영역 크기 구하고, 최댓값 비교

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 벽을 세울 수 있는 곳 구하기
# 바이러스 위치 구하기
walls = []
virus = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0: # 빈칸인 경우
            walls.append((i, j)) # walls 리스트에 담기
        elif maps[i][j] == 2: # 바이러스인 경우
            virus.append((i, j)) # virus 리스트에 담기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus_length = len(virus) # 바이러스 개수
walls_length = n*m - len(walls) - virus_length # 벽 개수
def bfs(walls):# 벽으로 변경할 3군데 리스트
    for x, y in walls: # 3군데 벽으로 변경
        maps[x][y] = 1

    visited = [[0] * m for _ in range(n)] # 방문처리를 위한 배열

    # 바이러스 퍼트리기
    queue = deque(virus)
    for x, y in virus: # 방문처리
        visited[x][y] = 1
    virus_cnt = virus_length # 바이러스 초기 개수

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 바이러스 상하좌우 인접한 칸으로 퍼짐
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 1: # 범위 안에 있고, 아직 바이러스가 한번도 퍼지지 않았으며, 벽이 아닌경우
                visited[nx][ny] = 1 # 바이러스 퍼짐
                queue.append((nx, ny)) # 큐에 추가
                virus_cnt += 1 # 바이러스 개수 1 추가

    # 다시 maps 원상태 복구
    for x, y in walls:
        maps[x][y] = 0 # 다시 빈칸으로 변경

    return (n * m) - virus_cnt - (walls_length + 3) # 전체 넓이 - 바이러스 퍼진 공간 넓이 - (원래 벽 개수 + 3)

answer = 0 # 안전 영역 크기의 최댓값
for wall in combinations(walls, 3):
    # bfs를 사용해서 3군데 벽으로 변경하고, 바이러스 퍼트리고, 안전 영역 크기 반환 받기
    answer = max(answer, bfs(wall))

print(answer)

# 풀이 2
# import copy로 copy.deepcopy(2차원배열)을 통해서 깊은 복사로 새로운 maps를 만든다
# 바이러스 퍼트리고
# list.count(0)을 사용해서 각 행의 0의 개수(바이러스 안 퍼진곳)를 모두 더한다
# max 값과의 비교를 수행

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 벽을 세울 수 있는 곳 구하기
# 바이러스 위치 구하기
import copy

walls = []
virus = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0: # 빈칸인 경우
            walls.append((i, j)) # walls 리스트에 담기
        elif maps[i][j] == 2: # 바이러스인 경우
            virus.append((i, j)) # virus 리스트에 담기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(walls):
    # tmp_maps = copy.deepcopy(maps) # copy.deepcopy를 통한 깊은 복사 - 속도 느림
    tmp_maps = [map_row[:] for map_row in maps]  # slicing을 이용한 깊은 복사 - 속도 빠름
    for x, y in walls: # 3군데 벽으로 변경
        tmp_maps[x][y] = 1

    queue = deque(virus)
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 바이러스 상하좌우 인접한 칸으로 퍼짐
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tmp_maps[nx][ny] == 0:  # 범위 안에 있고, 빈 칸이라면(바이러스 안퍼졌고, 벽이 아닌 곳)
                tmp_maps[nx][ny] = 2  # 바이러스 퍼짐
                queue.append((nx, ny))  # 큐에 추가

    # 바이러스 모두 퍼트린 뒤에도 빈칸인 곳의 개수 세기
    cnt = 0
    for i in range(n):
        cnt += tmp_maps[i].count(0)

    # answer과의 비교를 통해서 최댓값 갱신
    global answer
    answer = max(answer, cnt)

answer = 0 # 안전 영역 크기의 최댓값
for wall in combinations(walls, 3):
    # bfs를 사용해서 3군데 벽으로 변경하고, 바이러스 퍼트리고, 안전 영역 크기 반환 받기
    bfs(wall)

print(answer)

# 풀이 1도 n*m 크기의 visited 배열을 매 bfs함수를 실행할 때마다 만들고, 풀이2도 tmp_maps를 만들기에 메모리는 유사한 듯하다.