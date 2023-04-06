import sys

input_data = sys.stdin.readline

N = int(input_data())
dp = [0, 1]     # dp[n]은 n을 표현하기 위한 최소 개수의 제곱수 합

for i in range(2, N+1):
    _min = 1e9
    j = 1
    while j**2 <= i:
        _min = min(_min, dp[i-j**2])    # 최소 개수의 제곱수 합을 구하기 위해 min 사용
        j += 1
    dp.append(_min + 1)     # dp[i]를 넣어줌
print(dp[N])

