import sys
from itertools import combinations


def chicken_dis(a, chicken):    # 집의 치킨 거리 구하는 함수
    min_dis = 5000
    for c in chicken:   # 치킨 집에 돌아가는 for 문
        dis = abs(c[0] - a[0]) + abs(c[1] - a[1])   # 치킨 집과의 거리
        min_dis = min_dis if min_dis < dis else dis     # 최소 거리 구하기
    return min_dis


input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]  # 도시 정보 입력 받기
one = []
two = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            one.append([i, j])  # one에 집 저장
        elif city[i][j] == 2:
            two.append([i, j])  # two에 치킨집 저장
combi = list(combinations(two, M))  # M개의 치킨집을 선택하는 조합 구하기
min_city_dis = 5000
for c in combi:    # M개의 치킨집 조합에 대해
    city_dis = 0
    for o in one:   # 각각의 집에 대한
        city_dis += chicken_dis(o, c)   # 치킨 거리 구하기
    min_city_dis = min_city_dis if min_city_dis < city_dis else city_dis    # 최소 도시의 치킨 거리 구하기
print(min_city_dis)
