import sys

N, T = map(int, sys.stdin.readline().split())
result = 0
carrots = []
for i in range(N):
    w, p = map(int, sys.stdin.readline().split())
    result += w     # 당근은 모두 먹기 때문에 초기맛 더하기
    carrots.append(p)   # 리스트에 저장
carrots.sort()      # 오름차순 정렬
for i in range(T-N, T):
    result += carrots[i-(T-N)] * i  # p가 크면 이후에 재배
print(result)


# 최대 힙 풀이
import heapq
N, T = map(int, input().split())
carrots = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
c = []
for i in range(N):
    heapq.heappush(c, (-carrots[i][1], carrots[i]))     # 최대 힙
result = 0
for i in range(T-1, -1, -1):
    result += c[0][1][0] + heapq.heappop(c)[1][1] * i
    if len(c) == 0:
        break
print(result)
