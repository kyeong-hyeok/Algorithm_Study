import sys

input_data = sys.stdin.readline

N = int(input_data())
apart = [list(map(int, input_data().strip())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []


def dfs(x, y):
    if 0 > x or x >= N or 0 > y or y >= N or apart[x][y] != 1:
        return 0
    count = 1
    apart[x][y] = 2    # 단지 결정되면 2로 변경
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        count += dfs(nx, ny)
    return count


for i in range(N):
    for j in range(N):
        if apart[i][j] == 1:    # 단지가 결정되지 않은 집이 있는 곳
            result.append(dfs(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

