import sys

input = sys.stdin.readline

N, K = map(int, input().split()) # N: 물품의 수, K: 준서가 버틸 수 있는 무게
items = []
for _ in range(N):
    W, V = map(int, input().split()) # W: 무게, V: 가치
    items.append((W, V))

knapsack = [[0 for _ in range(K+1)] for _ in range(N)] # dp 테이블 - 가로: 견딜 수 있는 무게, 세로 : 물건의 번호

for i in range(N):
    weight = items[i][0] # 물건의 무게
    value = items[i][1] # 물건의 가치
    knapsack[i][:weight] = knapsack[i-1][:weight] # 물건의 무게보다 작은 부분은 이전 열을 그대로 가져옴
    for j in range(weight, K+1):# 물건의 무게보다 크거나 같은 부분에 대해서
        knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j]) # max(현재 물건의 가치 + 현재 물건의 무게를 제외한 무게에서의 최대 가치, 이전 물건까지의 최대 가치)


print(knapsack[N-1][K])


# dp어렵다...
# dp : 큰 문제를 작은 문제로 쪼개서 그 답을 저장해두고 재활용. 기억하며 풀기.
# dp 사용할 때 : 동일한 작은 문제 들이 반복하여 나타나는 경우

