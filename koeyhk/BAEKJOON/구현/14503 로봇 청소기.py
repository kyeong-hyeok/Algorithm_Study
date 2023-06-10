import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
r, c, d = map(int, input_data().split())
room = []
for i in range(N):
    room.append(list(map(int, input_data().split())))
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def dfs(x, y, d):
    result = 0
    if room[x][y] == 0:
        room[x][y] = 2
        result += 1
    blank = 0
    for _ in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            blank = 1
            result += dfs(nx, ny, d)
            break
    if blank == 0:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] != 1:
            result += dfs(nx, ny, d)
    return result


print(dfs(r, c, d))