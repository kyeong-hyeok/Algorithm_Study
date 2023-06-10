import sys

input = sys.stdin.readline
H, W = map(int, input().split()) # 최대 높이, 가로 길이
arr = list(map(int, input().split())) # 높이들

# ==== 내 정답)
left = []
right = [0] * (W)

# 맨 왼쪽부터 각 위치까지의 높이 중 가장 높은 위치를 저장
_max = 0
for i in range(W):
    _max = max(_max, arr[i])
    left.append(_max)

# 맨 오른쪽부터 각 위치까지의 높이 중 가장 높은 위치를 저장
_max = 0
for i in range(W-1, -1, -1):
    _max = max(_max, arr[i])
    right[i] = _max

# 각 위치마다 왼쪽 높이와 오른쪽 높이 중 더 낮은 높이 - 본인의 높이를 sum에 더하기
sum = 0
for i in range(W):
   sum += min(left[i-1], right[i-1]) - arr[i-1]

# 결과 출력
print(sum)

# W <= 500이라서 순차탐색해도 시간복잡도 상으로 괜찮은 듯 하다.


# ==== 더 짧은 정답)
sum = 0
for i in range(1, W-1): # 어짜피 맨 처음과 맨 끝은 물이 채워질 수 없기에 제외
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    water_height = min(left_max, right_max) # 최대로 채워질 수 있는 물의 높이 = 왼쪽, 오른쪽 max 중에서 min값

    if arr[i] < water_height: # arr[i]가 water_hegiht보다 높을 수 있는 가능성도 있어서 해당 if문 작성 필요
        sum += water_height - arr[i]
print(sum)
