# 3:24 - 3:45
import sys
input = sys.stdin.readline

INF = int(1e9) # 무한대 상수

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

# 각 도시에서 도시로 가는 최단 비용이 담긴 그래프, 초기값은 모두 무한으로 설정
cost_graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신의 도시로 이동하는 비용은 0
for i in range(1, n + 1):
    cost_graph[i][i] = 0

# m개의 버스 정보를 받아서, 최단 비용 그래프 갱신
for _ in range(m):
    a, b, c = map(int, input().split())
    cost_graph[a][b] = min(cost_graph[a][b], c) # 주의) 시작도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다는 조건 때문에 해당 코드 필요

# 플로이드 워셜 알고리즘
def floyd_warshall():

    for k in range(1, n+1): # k를 거쳐서 가는 경로를 고려
        for a in range(1, n+1):
            for b in range(1, n+1):
                cost_graph[a][b] = min(cost_graph[a][b], cost_graph[a][k] + cost_graph[k][b]) # a에서 b로 직접가는 경우와, a에서 k를 거쳐 b로 가는 경우 중 최단 비용으로 갱신


floyd_warshall()

# 모든 경우의 최단 비용 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if cost_graph[i][j] == INF: # 도달할 수 없는 경우에는 0 출력
            print(0, end = " ")
        else:
            print(cost_graph[i][j], end = " ")
    print()





