# 못품

# idea
# dist, weak의 길이가 생각보다 짧음 -> 완전 탐색 -> 순열, 조합 많이 같이 쓰임
# 원형 -> 2배로 늘려서 원형을 일자로 만들어줌

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak += [w + n for w in weak] # 원형을 선형으로
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾기 위한 초기값 설정

    # 각 weak point 위치를 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대해서
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            position = weak[start] + friends[count-1] # 해당 친구가 점검할 수 있는 마지막 위치

            for index in range(start, start + length): # 시작 weak point idx에서 시작해서 weak length만큼
                if position < weak[index]: # 점검 가능한 위치 < weak point라면
                    count += 1 # 친구 추가
                    if count > len(dist): # 친구를 더 이상 추가할 수 없다면
                        break # 중지
                    position = weak[index] + friends[count-1] # 친구 추가했으니까, 해당 친구가 점검할 수 있는 마지막 위치 update
            answer = min(answer, count) # 최솟값 찾아서

    if answer > len(dist): # 친구 모두 투입해도 취약지점 전부 점검 불가능한 경우
        return -1
    return answer
