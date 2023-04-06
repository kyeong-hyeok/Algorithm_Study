# 11:53 - 12:13

N = int(input())  # 좌석의 개수
M = int(input())  # 고정석의 개수
vip = [int(input()) for _ in range(M)] + [N + 1]  # 고정석 번호, 오름차순 정렬되어 들어옴

dp = [0] * (N + 1)  # 고정석이 없을 경우의 각 번호에서 가능한 경우의 수
dp[0] = dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]  # 점화식

pre_v = 0  # 이전 vip 번호
answer = 1  # vip번호 사이의 구간에서 가능한 경우의 수를 곱해줄 것이라서 초기값 1로 설정
for v in vip:
    answer *= dp[v - pre_v - 1]  # vip 번호 사이의 구간에서 가능한 경우의 수
    pre_v = v  # 이전 vip 번호 갱신

print(answer)
