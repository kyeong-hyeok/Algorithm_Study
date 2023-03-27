N, M = map(int, input().split()) # N: 나무의 수, M: 가져가려는 나무의 길이
arr = list(map(int, input().split()))

# 절단기 높이 h일 때, 가져갈 수 있는 나무의 길이 반환
def calc_tree(h):
    total = 0
    for a in arr:
        cut = a - h
        total += cut if cut > 0 else 0 # 가져갈 수 있는 길이를 total에 더한다.

    return total

def binary_search():
    start, end = 1, max(arr) # 1, 현재 나무 중 최대 높이

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        if calc_tree(mid) >= M: # 현재 mid의 높이로 설정했을 때, M이상 가져갈 수 있다면
            answer = mid # 조건 만족했으니까 일단 answer 후보로 저장
            start = mid + 1 # 절단기 높이를 더 높게 설정
        else: # 현재의 절단기 높이로는 원하는 만큼 가져가지 못한다면
            end = mid - 1 # 절단기 높이 더 낮게 설정
    return answer

print(binary_search())

