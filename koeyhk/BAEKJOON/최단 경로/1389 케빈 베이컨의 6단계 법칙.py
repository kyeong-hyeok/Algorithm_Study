import sys
import heapq

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input_data().split())
    graph[a].append(b)
    graph[b].append(a)


def dijkstra(start):
    q = []
    distance = [1e9] * (N + 1)
    distance[0] = 0
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return sum(distance)


min_d = 1e9
for i in range(1, N + 1):
    d = dijkstra(i)
    if d < min_d:
        min_d = d
        min_p = i

print(min_p)
