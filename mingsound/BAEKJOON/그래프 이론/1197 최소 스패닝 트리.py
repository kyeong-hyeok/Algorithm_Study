# 8:48 - 9:05

v, e = map(int, input().split()) # 정점 수, 간선 수 입력받기

# 모든 간선에 대해서 (가중치, a, b)형식으로 저장
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선 가중치 기준 오름차순 정렬
edges.sort()

# 부모 테이블 초기화 : 자기자신으로 초기화
parent = [i for i in range(v+1)]

# 최소 스패닝 트리의 가중치
cost = 0

# 부모 정점 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# a, b 두개의 정점 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # 더 작은 부모의 정점을 가진쪽으로 합치기
        parent[b] = a
    else:
        parent[a] = b

# 모든 간선에 대해서
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # a, b를 연결해도 사이클이 생기지 않는다면
        union_parent(parent, a, b) # a, b 두개의 정점 합치기
        cost += c # 정답에 가중치 더하기

# 정답 출력
print(cost)