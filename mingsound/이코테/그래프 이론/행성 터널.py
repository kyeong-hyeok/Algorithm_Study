import copy

# 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두개의 정점 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())  # 행성의 개수

# 좌표를 xlist, ylist, zlist에 별도 저장
xlist, ylist, zlist = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    xlist.append((x, i))
    ylist.append((y, i))
    zlist.append((z, i))

xlist.sort()
ylist.sort()
zlist.sort()

# 간선 구성
# edge = (가중치, a행성, b행성)
edges = []
for curList in xlist, ylist, zlist:
    for i in range(1, n):
        w1, a = curList[i - 1]
        w2, b = curList[i]
        edges.append((abs(w1 - w2), a, b))

# 간선 가중치 기준 오름차순
edges.sort()

# 초기 부모노드 본인으로 설정
parent = [i for i in range(n)]


# 최소 신장 트리 만드는 알고리즘
# 1. edge를 최소 비용 정렬
# 2. 사이클 안 생기면, 두 개 행성 연결
def kruskal():
    result_cost = 0

    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 생기지 않았다면
            union_parent(parent, a, b)  # 두개의 행성 잇고
            result_cost += cost  # 최종 가중치 합계에 해당 가중치 포함

    print(result_cost)

kruskal()