import sys

input_data = sys.stdin.readline

V, E = map(int, input_data().split())
graph = []
parent = [i for i in range(V+1)]
for i in range(E):
    A, B, C = map(int, input_data().split())
    graph.append((C, A, B))
graph.sort()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
for i in graph:
    cost, a, b = i[0], i[1], i[2]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
print(result)
