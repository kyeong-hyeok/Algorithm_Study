import sys
sys.setrecursionlimit(10000)
input_data = sys.stdin.readline

n = int(input_data())
stair = []
for _ in range(n):
    stair.append(int(input_data()))
dp = [0]*(n+1)


def max_grade(x):   # 마지막 계단을 x로 하는 점수의 최댓값
    if dp[x] != 0:
        return dp[x]
    # x-3까지 밟고 x-1, x 계단 | x-2까지 밟고 x 계단 중 최댓값 저장
    dp[x] = max(max_grade(x-3) + stair[x-1], max_grade(x-2)) + stair[x]
    return dp[x]


if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    print(max_grade(n-1))
