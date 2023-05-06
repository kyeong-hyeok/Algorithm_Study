import sys
import heapq

input_data = sys.stdin.readline

INF = int(1e9)
N, D = map(int, input_data().split())
graph = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)
for i in range(N):
    a, b, c = map(int, input_data().split())
    if b > D:       # 도착 위치가 고속도로의 길이보다 크다면 추가 x
        continue
    graph[a].append((b, c))

for i in range(D):
    graph[i].append((i + 1, 1))     # 지름길 없다면 -> 1km 가는데 1km 소요


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(0)
print(distance[D])
