# 6:37 - 7:04, 7:28 - 7:54, 2:34 - 2:41

# 같은 시간에 진행하는 회의의 최대 개수 출력
import heapq

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda x: x[0]) # 시작 시간 기준 오름차순 정렬

h = [] # 최소 힙
_max = 0 # 최대 회의실 개수
_cnt = 0 # 현재시각에 필요한 회의실 개수
for start, end in arr:
    while h and h[0] <= start:# 끝낼 수 있는 회의는 모두 끝내기
        heapq.heappop(h)
        _cnt -= 1

    heapq.heappush(h, end)
    _cnt += 1
    if _max < _cnt:
        _max = _cnt

print(_max)

