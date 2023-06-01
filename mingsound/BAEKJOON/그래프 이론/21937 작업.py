# 문제 조건 : 사이클은 없다


# 해결 IDEA 1) 위상정렬
# 작업 X가 root라고 생각하고 작업 X에서 나가는 화살표로 도착하는 정점들에 대해서 진입차수가 0인 노드를 만날 때까지 계속해서 각 정점의 진입차수를 더해준다
# 결론 : 예제 3에 대해서 틀린 답이 나온다.
# => 구해야하는 것은 끝내야하는 작업 수(=정점 수)인데, 진입차수 개수(= 간선의 개수)를 세다보니까 에러가 발생
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 작업할 개수, M 순서정보 개수
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1) # 진입차수 배열
for _ in range(M):
    a, b = map(int, input().split()) # b작업을 하기전에 반드시 a 작업을 끝내야함
    graph[b].append(a) # a <- b
    indegree[b] += 1 # b의 진입차수 1증가
X = int(input())

def dfs(v):
    if indegree[v] == 0:
        return 0
    sum = 0
    for u in graph[v]:
        sum + dfs(u)

    return sum + indegree[v]

print(dfs(X) + indegree[X])
'''

# 해결 IDEA 2) 거꾸로 그래프 + DFS, BFS
# 간선을 거꾸로 저장하고, X에서 출발해서 DFS, BFS로 방문한 정점의 수를 세면 된다.
import sys
sys.setrecursionlimit(10**5)
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # N : 작업할 개수, M 순서정보 개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) # b작업을 하기전에 반드시 a 작업을 끝내야함
    graph[b].append(a) # a <- b, 거꾸로 그래프
X = int(input()) # 출발 정점

visited = [False] * (N+1)

## dfs 버전
def dfs(v):

    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            dfs(u)

## bfs 버전
def bfs(v):
    queue = deque([v])
    # visited[v] = True # X작업을 끝내기 위해 먼저 해야하는 작업 수라서 시작정점은 개수 포함 X, 그리고 어짜피 싸이클 없어서 시작정점 다시 방문 안한다는 확신이 있어서 방문처리 안해줘도 됨

    while queue:
        x = queue.popleft()

        for u in graph[x]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

bfs(X)
print(sum(visited))


