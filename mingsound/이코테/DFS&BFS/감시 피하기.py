# 4:48 - 5:04

# 선생님(T), 학생(S), 장애물(O)
# 3개의 장애물을 설치해서, 모든 학생들이 감시를 피할 수 있는지 여부

# idea
# 연구소 문제와 유사.
# combination 사용해서 장애물 3군데 설치 후, 선생님이 찾을 수 있는지 체크

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input()) # N x N 크기의 복도
graph = [list(input().rstrip().split()) for _ in range(N)] # 복도 정보

# 장애물 설치 가능 장소 obstacle 리스트에 추가
# 선생님 위치 teacher 리스트에 추가
obstacle = []
teacher = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            obstacle.append((i, j))
        elif graph[i][j] == 'T':
            teacher.append((i, j))

# 모든 학생이 선생님 감시 피할 수 있는지 여부 체크
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check():
    for x, y in teacher:
        for i in range(4): # 4방향 검사
            for j in range(1, 6): # 한방향으로 쭉 이동하면서 검사
                nx = x + (j * dx[i])
                ny = y + (j * dy[i])

                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 'S':
                        return False # 감시 피할 수 없다면 False 반환
                    elif graph[nx][ny] == 'O':
                        break # 다음 방향 이동으로


    return True

for case in combinations(obstacle, 3):
    # 장애물 추가
    for x, y in case:
        graph[x][y] = 'O'

    if check(): # 하나의 case라도 모든 학생이 검사 피할 수있다면 YES 출력 후 종료
        print("YES")
        exit()

    # 장애물 제거
    for x, y in case:
        graph[x][y] = 'X'

print("NO")