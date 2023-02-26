# 11:12 - 11:16

# 요약
# N을 자릿수 기준으로 반으로 나눠, 왼쪽의 각 자릿수의 합 = 오른쪽의 각 자릿수의 합인 경우

import sys
input = sys.stdin.readline

arr = list(map(int, list(input().rstrip())))
mid = len(arr)//2

if sum(arr[:mid]) == sum(arr[mid:]):
    print("LUCKY")
else:
    print("READY")