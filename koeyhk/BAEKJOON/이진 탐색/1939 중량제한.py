import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
bridge = [[] for _ in range(N + 1)]
for i in range(M):
    x, y, w = map(int, input_data().split())
    bridge[x].append((y, w))  # 해당 섬 인덱스에 (연결된 섬, 무게 제한) 저장
    bridge[y].append((x, w))
start, end = map(int, input_data().split())  # 시작점, 끝점


def bfs(c):
    queue = deque()
    queue.append(start)  # 시작점
    visit = set()  # 방문 여부
    visit.add(start)
    while queue:
        x = queue.popleft()
        for y, w in bridge[x]:  # 해당 섬에 연결된 섬과 무게 제한 가져오기
            if y not in visit and w >= c:  # 방문하지 않았거나 무게 제한이 c보다 크거나 같은 경우
                visit.add(y)
                queue.append(y)
    return True if end in visit else False  # 방문한 곳에 도착 지점이 있다면 True


_min, _max = 1, 1000000000
result = 0
while _min <= _max:         # 이진 탐색
    mid = (_min + _max) // 2
    if bfs(mid):            # 시작 섬에서 끝 섬까지 물품 운반이 가능하다면
        result = mid        # 결과 값에 해당 중량 저장
        _min = mid + 1
    else:
        _max = mid - 1

print(result)


# BFS + 이진 탐색 문제로 중량을 조절하면서 BFS를 이용해 탐색해야 했다.
# 연결된 섬과 중량을 다루는 방식이 적합하지 않았고, 이에 따른 방문 여부에 대한 처리가 미흡했다.
# BFS를 다루는 연습이 더 필요하다!