import sys

input_data = sys.stdin.readline

N, C = map(int, input_data().split())
house = [int(input_data()) for _ in range(N)]
house.sort()


def binary_search(house, min_dis, max_dis):     # (집, 최소 거리, 최대 거리)
    result = 0
    while min_dis <= max_dis:   # 최소 거리 <= 최대 거리일 때
        current = house[0]      # 현재 집
        mid = (min_dis + max_dis) // 2  # 현재 설치 거리
        set = 1
        for h in house:
            if h - current >= mid:  # 사이의 거리가 현재 설치 거리보다 크거나 같을 때
                set += 1
                current = h
        if set >= C:    # C개보다 같거나 많이 설치했을 때
            result = mid    # 결과 값에 현재 설치 거리 저장
            min_dis = mid + 1   # 최소 거리에 (현재 설치 거리 + 1)을 저장
        else:
            max_dis = mid - 1   # 최대 거리에 (현재 설치 거리 - 1)을 저장
    return result


print(binary_search(house, 1, house[-1] - house[0]))