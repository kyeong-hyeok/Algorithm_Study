# 방법 1 - 이진 탐색 1200ms

import sys

input_data = sys.stdin.readline

N = int(input_data())
A = list(map(int, input_data().split()))
A.sort()

result = 0
for i in range(len(A)):
    tmp = A[:i] + A[i+1:]   # 해당 수를 제외한 리스트
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]  # 두 수의 합 저장
        if t == A[i]:
            result += 1
            break
        if t < A[i]:
            left += 1
        else:
            right -= 1
print(result)


# 방법 2 - 해시 2100 ms

N = int(input_data())
A = list(map(int, input_data().split()))
d = dict()
for i in range(len(A)):
    if A[i] in d:   # 해당 key가 존재한다면
        d[A[i]] += 1    # value + 1
    else:
        d[A[i]] = 1     # value = 1

result = 0
for i in A:
    for j in d:
        d[i] -= 1   # 해당 key의 value - 1
        d[j] -= 1
        sub = i - j
        # 두 수의 차가 존재하고, value가 1이상이며, (두 수가 같을 때 -> 해당 수의 value가 0보다 크거나 같아야 함)!
        if sub in d and d.get(sub, 0) >= 1 and d.get(i, -1) >= 0:
            result += 1
            d[i] += 1   # 해당 key의 원상복구
            d[j] += 1
            break
        d[i] += 1
        d[j] += 1
print(result)