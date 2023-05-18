from collections import deque

for _ in range(int(input())):
    n = int(input()) # 팀의 수

    graph = [[] for _ in range(n+1)] # 그래프
    indegree = [0] * (n + 1) # 진입차수
    queue = deque()
    answer = []
    flag = 0

    # 처음 주어진 순위기반으로 모든 정점마다 간선 연결
    # 순위 역전관계된 것들에 대해서만 순위가 변경되고, 나머지는 순위가 유지되어야하기에 모든 정점에 대해서 간선 연결
    ranking = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(i+1, n):
            graph[ranking[i]].append(ranking[j])
            indegree[ranking[j]] += 1

    # 순위 변경된 것들
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # a, b간의 순위가 명확하지 않아서 분기처리 필요
        flag = True

        # 순위 : a > b
        for x in graph[a]:
            if x == b:
                graph[a].remove(b)
                indegree[b] -= 1
                graph[b].append(a)
                indegree[a] += 1
                flag = False

        # 순위 : b > a
        if flag:
            for x in graph[b]:
                if x == a:
                    graph[b].remove(a)
                    indegree[a] -= 1
                    graph[a].append(b)
                    indegree[b] += 1

    # 큐 초기화 : 진입차수 0인 것들 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    # 초기 큐에 아무것도 없다면 사이클이 발생한 것 -> 위상관계 표현 불가능
    if not queue:
        print("IMPOSSIBLE")
        continue


    result = True
    while queue:
        if len(queue) > 1: # 한차례의 큐에 2개 이상의 원소가 들어갔다면 다양한 순위가 나올 수 있음
            result = False
            break

        # 큐에서 하나 꺼내서 정답 리스트에 넣기
        now = queue.popleft()
        answer.append(now)

        # 현재 정점과 연결된 정점들에 대해서 진입차수 감소 및 0이라면 큐에 넣기
        for x in graph[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)

    if not result or len(answer) < n: # 시작 노드가 없거나, 위상정렬을 끝냈는 데도 방문하지 않은 정점이 있다면 IMPOSSIBLE
        print("IMPOSSIBLE")
    else:
        print(*answer)

# 문제에서 확실한 순위를 찾을 수 없다면 '?'를 출력하라고 했지만, 이미 작년에 확실한 순위가 주어져서 해당 예외는 없다.