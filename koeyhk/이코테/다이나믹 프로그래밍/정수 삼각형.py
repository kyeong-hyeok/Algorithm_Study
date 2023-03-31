import sys

input_data = sys.stdin.readline

n = int(input_data())
tri = [list(map(int, input_data().split())) for _ in range(n)]
d = [[-1]*i for i in range(1, n+1)]     # 계산한 적 있는지 여부


def max_tri(x, y):
    if x == n-1:            # 제일 아래층인 경우
        d[x][y] = tri[x][y]
        return d[x][y]
    if d[x][y] != -1:       # 계산한 적 있는 경우
        return d[x][y]
    d[x][y] = max(max_tri(x + 1, y), max_tri(x + 1, y + 1)) + tri[x][y]     # 밑의 층까지의 최댓값에 해당 정수 더하기
    return d[x][y]


print(max_tri(0, 0))