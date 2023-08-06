import sys
from collections import deque

input_data = sys.stdin.readline

M, N, H = map(int, input_data().split())

box = [[] for _ in range(H)]    # 토마토 보관 창고
for i in range(H):
    for j in range(N):
        box[i].append(list(map(int, input_data().split())))

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:   # 익은 토마토 큐에 저장
                q.append((i, j, k, 0))

if len(q) == 0:     # 익은 토마토가 없다면 -1
    print(-1)
else:   # BFS
    while q:
        a, b, c, d = q.popleft()
        for i in range(6):  # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
            da, db, dc = a + dx[i], b + dy[i], c + dz[i]
            if 0 <= da < H and 0 <= db < N and 0 <= dc < M and box[da][db][dc] == 0:
                box[da][db][dc] = 1     # 토마토 익음
                q.append((da, db, dc, d+1))     # x, y, z, 익게 된 날짜
    p = 0
    for i in box:
        for j in i:
            if 0 in j:      # 안 익은 토마토가 존재한다면 p = 1
                p = 1
                break
        if p == 1:
            break
    if p == 1:
        print(-1)
    else:
        print(d)