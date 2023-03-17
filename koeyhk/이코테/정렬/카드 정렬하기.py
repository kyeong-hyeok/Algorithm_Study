import heapq
import sys

input = sys.stdin.readline

N = int(input())
deck = []
for _ in range(N):
    heapq.heappush(deck, int(input()))

result = 0
if len(deck) != 1:  # deck이 하나가 아닐 때
    while len(deck) >= 2:    # deck이 2개 이상일 때 돌아가는 while 문
        comp = heapq.heappop(deck) + heapq.heappop(deck)    # 작은 덱 두 개 꺼내서 비교
        result += comp      # 결과에 비교한 값 더하기
        heapq.heappush(deck, comp)  # 작은 덱 두 개를 합친 것을 다시 heappush
print(result)