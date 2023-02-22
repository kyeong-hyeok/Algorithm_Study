# 못품

# 정답 풀이
import heapq

def solution(food_times, k):

    # k초 뒤에는 모든 음식들이 남은시간 0인 경우
    if sum(food_times) <= k:
        return -1

    # 먹는 시간 작은 순
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # (먹는데 걸리는 시간, 순서)

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    while sum_value + ((q[0][0] - previous) * length) <= k: # 먹는데 걸리는 시간이 제일 작은 것을 다 먹었을 때도 k초가 되지 않는다면
        now = heapq.heappop(q)[0] # 가장 작은 먹는 시간
        sum_value += (now - previous) * length
        length -= 1 # 하나 다 먹었으니까, 남은 음식 개수 -1
        previous = now

    # 남은 음식들 중에서 몇 번째 음식인지 판단
    result = sorted(q, key = lambda x: x[1]) # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
