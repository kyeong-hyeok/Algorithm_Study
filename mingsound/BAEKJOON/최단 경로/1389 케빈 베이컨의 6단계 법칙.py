# 3:56 - 4:12

# idea
# 케빈 베이컨 수 = 해당 노드에서 다른 노드로 가는 최단 경로의 합
# -> 모든 노드 사이의 최단 경로를 구해야함 = 플로이드 워셜
# 시간복잡도 O(N^3) = O(100^3)

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())# 유저의 수, 친구 관계의 수

# 친구 관계 무한대로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로의 친구 관계는 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 친구 관계 1로 표시
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def floyd_warshall():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 플로이드 워셜 수행
floyd_warshall()

# 케빈 베이컨 수가 가장 작은 사람 찾기
_min = 1e9
answer = 0
for i in range(1, n+1):
    if sum(graph[i][1:]) < _min:
        _min = sum(graph[i][1:])
        answer = i

print(answer)


