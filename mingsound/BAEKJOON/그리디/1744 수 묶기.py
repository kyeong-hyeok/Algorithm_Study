# 못품

# 요약
# 수 2개씩 묶어서 서로 곱한뒤에 더함
# 꼭 2개씩 묶지 않아도 됨
# 합 최대가 되도록

# idea
# 최대한 큰 수끼리 묶는 것이 좋다.
# 다만 수 중에서 음수 있을 수 있음.
# 음수끼리 곱하면 양수가 된다.

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

plus = []
minus = []
for i in range(n):
    if arr[i] > 0:
        plus.append(arr[i])
    else:
        minus.append(arr[i])

plus.sort(reverse=True) # 양수는 내림차순 정렬
minus.sort() # 음수는 오름차순

answer = 0

plus_length = len(plus)
for i in range(0, plus_length, 2):
    if i == plus_length-1:
        answer += plus[i]
    elif plus[i] == 1 or plus[i+1] == 1:
        answer += (plus[i] + plus[i+1])
    else:
        answer += (plus[i] * plus[i+1])

minus_length = len(minus)
for i in range(0, minus_length, 2):
    if i == minus_length-1:
        answer += minus[i]
    else:
        answer += (minus[i] * minus[i+1])

print(answer)

# -- 다른 사람 풀이 --
# 차이점
# 1. 1은 양수배열에 넣지 않고, 그냥 answer에 +1을 해줌
# 2. 길이 홀짝을 나눠서 코드 작성

N = int(input())
positive = []
negative = []
answer = 0

for _ in range(N):
    n = int(input())

    if n > 1:
        positive.append(n)
    elif n == 1: # 1인 수들은 바로 더해준다.
        answer += 1
    else:
        negative.append(n)

# 정렬
positive.sort(reverse=True)
negative.sort()

# 양수 리스트 더해주기
if len(positive) % 2 == 0: # 양수가 짝수개 일경우 두개씩 곱해준다.
  for i in range(0, len(positive), 2):
    answer += positive[i] * positive[i+1]
else:
  for i in range(0, len(positive)-1, 2):
    answer += positive[i] * positive[i+1]
  answer += positive[len(positive)-1] # 마지막 수는 더해준다.

# 음수 더해주기
if len(negative) % 2 == 0: # 음수가 짝수개 일경우 두개씩 곱해준다.
  for i in range(0, len(negative), 2):
    answer += negative[i] * negative[i+1]
else:
  for i in range(0, len(negative)-1, 2):
    answer += negative[i] * negative[i+1]
  answer += negative[len(negative)-1] # 마지막 수는 더해준다.

print(answer)