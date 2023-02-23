import sys
import heapq

N = int(input())
time = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
time.sort(key=lambda x: x[0])   # 시작 시간을 기준으로 오름차순 정렬
end = [0]   # 회의실 끝나는 시간 저장
room = 1
for s, e in time:
    if s >= end[0]:     # 시작 시간과 가장 빨리 끝나는 회의실 시간 비교
        heapq.heappop(end)
    else:
        room += 1   # 회의실 하나 늘리기
    heapq.heappush(end, e)  # 끝나는 시간 추가하기
print(room)
