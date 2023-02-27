# 10:22 - 10:50

# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 0 : 빈칸, 1: 집, 2: 치킨집

# idea
# combination 사용해서 치킨집 m개 고르고, bfs 사용해서 치킨집에서 집까지의 최소거리 찾기

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            houses.append((i, j))
        elif maps[i][j] == 2:
            chickens.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(chicken):
    visit = [[0] * n for _ in range(n)]
    queue = deque(chicken)
    total = 0
    for q in queue:
        x, y = q
        visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and ((not visit[nx][ny]) or (visit[nx][ny] > visit[x][y] + 1)):
                 # 집이 아니라면 큐에 담기 -> 실패
                 # 집 바로 옆에 집이 있는 경우도 있을 수 있어서, 그냥 모든 곳에 대해서 치킨 거리를 구한다고 생각해야함
                queue.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    for x, y in houses:
        total += (visit[x][y] - 1)
    return total

m_chickens = list(combinations(chickens, m))
answer = float('inf')
for chicken in m_chickens:
    answer = min(answer, bfs(chicken))

print(answer)

# 다른 풀이 - 시간 더 빠름

# idea
# 치킨 집 m개 골라서, abs(x-y) 사용해서 각 집에서 치킨 집까지의 거리의 최솟값 찾기

n, m = map(int, input().split())
chickens = []
maps = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chickens.append((i, j))

answer = 1e9 # 큰 숫자
for chicken in list(combinations(chickens, m)): # 치킨집 m개 골라서
    total = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1: # 집이라면
                _min = 1000
                for x, y in chicken: # 치킨집까지의 거리의 최솟값 찾기
                    _min = min(_min, abs(i-x) + abs(j-y))
                total += _min # 치킨 거리 총합
    answer = min(answer, total)

print(answer)
