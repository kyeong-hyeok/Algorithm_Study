# 11:06 - 11:29

# 매 초마다 번호가 낮은 종류의 바이러스부터 증식
# 바이러스는 상하좌우 방향으로 1초마다 증식
# 이미 바이러스가 존재하는 경우, 다른 바이러스 들어갈 수 없다
# S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류 출력, 바이러스가 존재하지 않는다면 0 출력

# idea
# 바이러스 리스트에 (바이러스 종류, x, y) 를 담고, 바이러스 종류 기준 오름차순으로 정렬
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # k : 바이러스 종류(1~k)
graph = [list(map(int, input().split())) for _ in range(n)] # n x n 크기
S, X, Y = map(int, input().split())

# 바이러스 담기
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0: # 바이러스가 존재한다면
            virus.append((graph[i][j], i, j)) # 종류, 위치 튜플 형태로 담기

# 바이러스 종류 기준 오름차순으로 정렬
virus.sort(key = lambda x: x[0])
# 참고) virus.sort() : 맨 앞 원소 기준 오름차순 정렬

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque(virus)

    for t in range(S): # s초 동안
        tmp_queue = deque([]) # 매초 마다 퍼지는 곳 담는 새로운 큐

        while queue: # 1초 동안 바이러스 퍼트리기
            k, x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0: # 범위 안에 있고, 아직 바이러스가 퍼지지 않았다면
                    graph[nx][ny] = k # 바이러스 종류 graph에 기록
                    tmp_queue.append((k, nx, ny)) # 새로운 queue에 담기

        queue = tmp_queue # tmp_queue로 queue 변경

bfs()

print(graph[X-1][Y-1]) # 문제에서 맨 왼쪽이 (1, 1) 기준이라서