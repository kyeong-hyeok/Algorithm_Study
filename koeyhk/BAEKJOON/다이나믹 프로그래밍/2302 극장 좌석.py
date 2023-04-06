import sys

input_data = sys.stdin.readline

N = int(input_data())
M = int(input_data())

vip = [0]       # 처음에 VIP 좌석이 있다고 가정 -> 일반 좌석 개수 구할 때 편리함
for i in range(M):
    v = int(input_data())
    vip.append(v)
vip.append(N + 1)       # 끝에 VIP 좌석이 있다고 가정 -> 일반 좌석 개수 구할 때 편리함

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]  # 피보나치 수열

if M:                   # VIP 좌석이 있을 경우
    dif = []            # VIP 좌석 사이의 일반 좌석 개수
    for i in range(M + 1):
        dif.append(vip[i + 1] - vip[i] - 1)  # 일반 좌석 개수 저장
    result = 1
    for d in dif:
        result *= dp[d]  # 일반 좌석 개수에 해당하는 dp 값 곱하기
else:
    result = dp[N]      # VIP 좌석이 없다면 dp[N]

print(result)

# 1         1

# 1 2       2
# 2 1

# 1 2 3     2 1
# 1 3 2
# 2 1 3

# 1 2 3 4    2 1 2
# 1 2 4 3
# 1 3 2 4
# 2 1 3 4
# 2 1 4 3

# 1 2 3 4 5    2 1 2 2 1
# 1 2 3 5 4
# 1 2 4 3 5
# 1 3 2 4 5
# 1 3 2 5 4
# 2 1 3 4 5
# 2 1 3 5 4
# 2 1 4 3 5
