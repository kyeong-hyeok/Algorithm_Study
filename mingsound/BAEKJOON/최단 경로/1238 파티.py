import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split()) # 학생 수, 도로 수, 몇 번 마을

# 도로 정보 입력 받기
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    rev_graph[end].append((start, time))

INF = 1e9

# 특정 정점 S에서 다른 모든 정점까지의 최단거리 구하기
def dijkstra(start, graph):
    # 처음 초기값은 모두 INF로 설정
    distance = [INF] * (N + 1)

    # 시작 정점에 대해서 초기화
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start)) # 최단 거리, 정점

    # q에 데이터가 있는 동안
    while q:
        dist, now = heapq.heappop(q) # 최단 경로 정점 꺼내기

        if distance[now] < dist: # 이미 방문을 했다면 continue
            continue

        # now 정점과 연결된 정점들에 대해서
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

    return distance

answer = 0
# X에서 다른 정점까지의 최단경로가 담긴 배열
distance_from_X = dijkstra(X, graph)
distance_To_X = dijkstra(X, rev_graph)
for i in range(1, N+1):
    if i == X: # 시작정점이 모이기로 한 마을과 같다면, 경로가 X - X - X의 최단 경로니까 무조건 최소
        continue
    # max(answer, X에서 i로의 최단 경로 + i에서 X로의 최단 경로)
    answer = max(answer, distance_from_X[i] + distance_To_X[i])

print(answer)

# 시간복잡도 : O(N x ElogN) = O(1000 x 10000 log(1000)) = O(10^7 x 10) = O(10^8)
# log[2]{1000000} = 10
# log[2]{1000000} = 20

# 참고
# https://kangmin1012.tistory.com/8
