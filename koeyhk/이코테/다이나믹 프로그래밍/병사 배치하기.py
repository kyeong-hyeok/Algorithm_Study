# 가장 긴 증가하는 부분 수열(LIS) -> 가장 긴 감소하는 부분 수열로 변경
# 모든 0 <= j < i 에 대하여,
# dp[i] = max(dp[i], dp[j] + 1) if array[j] < array[i]

import sys

input_data = sys.stdin.readline

N = int(input_data())
soldier = list(map(int, input_data().split()))
soldier.reverse()       # LIS 사용하기 위해 배열 뒤집기

dp = [1] * (N+1)
for i in range(1, N):       # LIS 알고리즘 수행
    for j in range(0, i):
        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
