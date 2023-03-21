# 풀이 1 - 이진 탐색
import sys

input_data = sys.stdin.readline
T = int(input_data())


def Binary_search(A, target, start, end):   # 이진 탐색
    result = 0
    while start <= end:
        mid = (start + end) // 2    # 중간 인덱스 저장
        if A[mid] <= target:    # 배열 A의 원소 값이 타겟 값보다 작으면
            start = mid + 1     # 뒷부분 이진 탐색
        else:
            result = len(A) - mid   # target보다 크거나 같은 원소들의 총 개수 저장
            end = mid - 1   # 앞부분 이진 탐색
    return result


for i in range(T):
    N, M = map(int, input_data().split())
    A = list(map(int, input_data().split()))
    B = list(map(int, input_data().split()))
    A.sort()
    result = 0
    for i in B:
        result += Binary_search(A, i, 0, len(A)-1)
    print(result)

# 풀이 2 - 정렬

import sys

input_data = sys.stdin.readline

T = int(input_data())

for i in range(T):
    N, M = map(int, input_data().split())
    A = list(map(int, input_data().split()))
    B = list(map(int, input_data().split()))
    A.sort()
    B.sort()
    i = 0
    result = 0
    for a in A:     # A의 원소에 돌아가는 for 문
        while i < M and a > B[i]:   # 인덱스가 B의 크기보다 작고, A의 원소가 B의 해당 원소보다 클 때
            i += 1  # 인덱스 증가
        result += i     # 결과값에 더하기
    print(result)


# 속도 : 풀이 1 < 풀이 2