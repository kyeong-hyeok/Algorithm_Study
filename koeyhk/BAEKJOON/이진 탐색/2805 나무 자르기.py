import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
tree = list(map(int, input_data().split()))
tree.sort()     # 나무 높이 오름차순 정렬


def Binary_search(tree, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        length = 0
        for i in range(len(tree)-1, -1, -1):    # 높이가 큰 나무부터 순서대로 for 문
            if tree[i] > mid:       # mid보다 높이가 높다면
                length += tree[i] - mid     # 자른 뒤 더하기
            else:                   # mid보다 높이가 낮거나 같다면
                break               # 빠져 나오기
        if length >= M:        # 길이가 M보다 길다면
            start = mid + 1     # 절단기 높이 높게 설정
            result = mid        # 결과 값에 저장
        else:                   # 길이가 M보다 짧다면
            end = mid - 1       # 절단기 높이 낮게 설정
    return result


print(Binary_search(tree, 0, tree[-1]))

