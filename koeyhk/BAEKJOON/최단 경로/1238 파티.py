import sys
import heapq

input_data = sys.stdin.readline

INF = int(1e9)
N, M, X = map(int, input_data().split())
graph = [[] for _ in range(N + 1)]
time = [INF] * (N + 1)
for i in range(M):
    a, b, c = map(int, input_data().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    time[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        t, now = heapq.heappop(q)
        if time[now] < t:
            continue
        for i in graph[now]:
            cost = t + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


total_time = [0] * (N + 1)      # 오고 가는데 소비하는 총 시간
for i in range(1, N + 1):
    time = [INF] * (N + 1)
    dijkstra(i)                 # 각 학생마다 출발지 결정
    total_time[i] = time[X]     # i번 마을에서 X번 마을에 가는데 걸리는 시간

time = [INF] * (N + 1)
dijkstra(X)     # X번 마을에서 각 마을로 가는데 걸리는 시간 찾기
for i in range(1, N+1):
    total_time[i] += time[i]    # 자신의 마을로 돌아가는 시간 더해주기

print(max(total_time))      # 가장 오래 걸리는 학생의 소요시간 출력