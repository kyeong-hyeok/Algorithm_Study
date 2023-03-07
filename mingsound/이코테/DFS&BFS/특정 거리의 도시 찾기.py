# 8:58 - 9:16

# bfs 사용
# visited 배열은 1차원으로 만든다.

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):  # 매개변수: 출발도시 정점 번호
    queue = deque([x])
    visited[x] = 1  # 방문처리

    while queue:
        x = queue.popleft()

        for v in graph[x]:  # x와 연결된 모든 정점 방문
            if not visited[v]:  # 아직 방문하지않은 인접 정점들에 대해서
                visited[v] = visited[x] + 1  # 최단거리 기록이자, 방문처리
                queue.append(v) # 큐에 추가

                # visited에 방문하지 않은 경우에 0을 사용하기에, visited에 최단거리+1의 값이 저장되어있음
                if visited[v] == (k + 1):  # 최단거리가 k인 경우
                    answer.append(v)  # answer 배열에 추가


n, m, k, x = map(int, input().split()) # 정점 수, 간선 수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)] # 정점 1부터 시작하기 때문에 n+1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 방향 그래프

visited = [0] * (n+1) # 정점 1부터 시작하니까 n+1
answer = [] # 최단거리 k인 정점들 담을 리스트

bfs(x) # bfs 수행

if not answer: # 빈 배열인 경우 = 최단거리가 k인 도시가 하나도 없는 경우
    print(-1)
else: # 최단 거리 k인 도시 있는 경우
    for x in sorted(answer): # 오름차순 정렬 후 출력
        print(x)


# 풀이 2) 다익스트라 사용
# 다익스트라 : 하나의 시작 정점으로 부터 모든 다른 정점까지의 최단 경로 찾기
import heapq

INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1) # 시작정점으로부터 각 정점까지의 최단 거리 기록하는 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # (정점, a-b사이 간선의 가중치)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 최소힙에 (0, 시작정점번호) 추가
    distance[start] = 0 # 시작 값 0으로 초기화

    while queue: # queue가 빌 때까지
        dist, now = heapq.heappop(queue)
        if distance[now] < dist: # 현재 시작정점에서 now까지의 최소거리 < queue에 저장할 때의 시작정점에서 now까지의 최소거리
            continue # if문 아래 코드는 now 정점을 거쳐서 갈 때 이득을 보는 경우를 알아보기 위함이므로

        for j in graph[now]: # now 정점의 모든 인접 정점들에 대해서
            cost = dist + j[1] # now를 거쳐서 인접 정점에 갈 때 거리 값
            if cost < distance[j[0]]: # now 거쳐서 j까지 가는 거리 값 < 현재 저장된 시작정점에서 j까지 최소 거리 값 이라면
                distance[j[0]] = cost # 시작정점에서 j까지의 최소 거리 값 update
                heapq.heappush(queue, (cost, j[0]))

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i)