# 8:19 - 8:35

# 그래프 상에서 선후관계가 있다면, 위상 정렬을 수행해 모든 선후 관계를 지키는 전체 순서를 계산할 수 있다.

from collections import deque

n, m = map(int, input().split())  # 과목의 수(정점 수), 선수 조건의 수(간선 수) 입력 받기
graph = [[] for _ in range(n + 1)]  # 그래프 선언
indegree = [0] * (n + 1)  # 각 정점의 진입차수 개수 리스트

# 선수 조건(간선) 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1  # 진입차수 계산


# 위상정렬
def topology_sort():
    result = [0] * (n + 1)  # 정답리스트: 문제의 답을 기록
    q = deque([])  # 진입차수가 0인 정점을 담는 큐

    # 큐 초기화 : 진입차수가 0인 정점을 큐에 담는다
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cnt = 1  # 학기
    while q:  # 매학기 마다
        tempq = deque([])  # 다음학기에 들을 수 있는 것(다음 턴에 진입차수 0인 정점 담을 큐)

        # 현재 학기에 들을 수 있는 과목마다
        for now in q:
            result[now] = cnt  # 해당 과목듣는 학기 정답리스트에 기록

            for x in graph[now]:  # 현재학기에 듣는 과목이 선수과목인 과목들에 대해서 진입차수 감소
                indegree[x] -= 1
                if indegree[x] == 0:  # 만약 진입차수가 0이라서 다음학기에 수강 가능하면 tempq에 넣기
                    tempq.append(x)

        # 다음 턴을 위한 update
        q = tempq  # q <-> tempq 바꿔치기
        cnt += 1  # 학기 증가

    print(*result[1:])  # 정답 출력


# 방법 2) 차이점 : q에 저장시 (정점, cnt)와 같은 튜플형태로 저장
def topology_sort2():
    result = [0] * (n + 1)  # 정답리스트: 문제의 답을 기록
    q = deque([])  # 진입차수가 0인 정점을 담는 큐

    # 큐 초기화 : 진입차수가 0인 정점을 큐에 담는다
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 1))

    while q:
        now, cnt = q.popleft()
        result[now] = cnt

        for x in graph[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append((x, cnt + 1))

    print(*result[1:])


topology_sort()