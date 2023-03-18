import sys
from itertools import combinations

# 0 : 빈칸, 1 : 벽, 2 : 바이러스
# 바이러스가 퍼져나간 길이가 최소여야함
# 벽 3개를 조합으로 결정

input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
zero = []
two = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:      # 빈칸인 부분
            zero.append([i, j])
        if lab[i][j] == 2:      # 바이러스인 부분
            two.append([i, j])

combi = list(combinations(zero, 3))     # 빈칸인 부분에서 3개를 고른 조합


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return
    if lab1[x][y] == 0:       # 빈칸인 부분일 때
        lab1[x][y] = 2
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)


answer = 0
for c in combi:
    lab1 = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            lab1[i][j] = lab[i][j]      # 지도의 복사본
    for i, j in c:
        lab1[i][j] = 1      # 벽 세우기
    for x, y in two:    # 바이러스가 있는 곳 주변에 dfs 함수 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    safe = 0        # 안전 영역
    for i in range(N):
        for j in range(M):
            if lab1[i][j] == 0:
                safe += 1
    answer = max(answer, safe)      # 안전 영역의 최대 크기 구하기

print(answer)
