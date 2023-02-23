# 12:18 - 12:22

# 요약
# |A-B| 불만도
# 불만도의 총합을 최소로하면서 등수매기고 싶음

# idea
# 예상 등수와 실제 등수가 차이가 적을 수록 이득
# 예상 등수 오름차순 정렬, 실제 등수는 1부터 순차 배열로 생각. |실제 등수 - 예상 등수| 총합 계산하면 될듯

import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

answer = 0
for i in range(1, n+1):
    answer += abs(arr[i-1] - i)

print(answer)

