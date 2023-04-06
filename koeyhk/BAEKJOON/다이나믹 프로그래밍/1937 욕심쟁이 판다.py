import sys
sys.setrecursionlimit(1000000)
input_data = sys.stdin.readline

N = int(input_data())
tree = [list(map(int, input_data().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dp = [[0] * N for _ in range(N)]


def dfs(x, y):
    if dp[x][y]:        # dfs 수행한 칸이라면 반환
        return dp[x][y]
    dp[x][y] = 1        # 초기값 1로 설정(이동 불가능한 칸 -> 1)
    for i in range(4):      # 상하좌우
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and tree[x][y] < tree[nx][ny]:   # 조건을 만족한다면
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)       # 해당 칸의 dp값과 (상하좌우 방향의 dp값 + 1) 중 최댓값 저장
    return dp[x][y]


_max = 0
for i in range(N):
    for j in range(N):
        _max = max(_max, dfs(i, j))     # 최대 dp값 구하기

print(_max)