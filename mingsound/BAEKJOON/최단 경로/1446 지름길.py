import heapq
import sys

input = sys.stdin.readline

# 특정지점 0에서 특정지점 D까지의 거리의 최소 값을 구하는 문제 => 다익스트라

# 지름길 개수, 고속도로 길이
N, D = map(int, input().split())

# 최단 거리 그래프를 초기에는 모두 INF로 설정
INF = 1e9
distance = [INF] * (D + 1)

# 각 거리마다 다음 거리까지의 최소 이동거리는 1
graph = [[] for _ in range(D + 1)]
for i in range(D):
    graph[i].append((i + 1, 1))  # end, dist

# 지름길 추가
for i in range(N):
    start, end, dist = map(int, input().split())
    if end > D:  # D보다 큰 곳이 end인 지름길은 의미없음
        continue
    graph[start].append((end, dist))


# 다익스트라 알고리즘 O(ElogV)
def dijkstra():
    h = []
    # 초기 위치 0에 대해서
    heapq.heappush(h, (0, 0))  # 방문하지 않은 것중에서 최단거리를 뽑아내는 heap에 추가
    distance[0] = 0  # 최단 거리 그래프에 초기 위치 초기화

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:  # 이미 최단 경로 확정된 경우를 재방문한 경우
            continue

        # 현재 now와 이어진 모든 정점 x에 대해서
        for x in graph[now]:
            cost = dist + x[1]  # now를 거쳐서 가는 경우 최단 경로 구하기

            # now를 거쳐서 가는 경우에 더 최단 경로라면
            if distance[x[0]] > cost:
                distance[x[0]] = cost  # 최단 경로 그래프 갱신
                heapq.heappush(h, (cost, x[0]))  # heap에 추가


dijkstra()
print(distance[D])