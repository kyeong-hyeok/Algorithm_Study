# 3:38 - 4:21, 4:28 - 5:13

# 요약
# 처음에는 (1, 1), 오른쪽을 향해 있다
# 이동은 머리를 다음 칸에 두고, 다음 칸에 사과가 있으면 그대로 두고, 사과가 없다면 꼬리를 땡긴다
# 벽 또는 자기자신의 몸과  부딪히면 게임이 끝난다

# idea
# 뱀은 deque사용해서 좌표 저장하면 될 것 같음

# 중요
# 예제3) 머리먼저 이동해서 꼬리 이동하기전에 머리와 꼬리가 부딫칠 수 있음

import sys
from collections import deque
input = sys.stdin.readline
snake = deque([(1, 1)]) # 위치

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
apple = set([tuple(map(int, input().rstrip().split())) for _ in range(K)]) # 사과의 위치
# 참고) set의 요소로 tuple은 가능한데 list는 안됨. 즉 set(2차원 배열)은 불가능
L = int(input())
move = []
for _ in range(L): # 초는 정렬된 상태로 주어져서 별도의 정렬이 필요 없다
    arr = list(input().rstrip().split())
    move.append((int(arr[0]), arr[1]))

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0 # 처음에는 오른쪽을 바라보고 있다
cnt = 0 # 시간
m = 0 # move 인덱스

while True:
    x, y = snake[0]
    nx = x + dx[dir]
    ny = y + dy[dir]
    cnt += 1
    # 벽에 부딫치지 않았고, 자신의 몸에도 부딫치지 않았다면
    if 1 <= nx <= N and 1 <= ny <= N and (nx, ny) not in snake:
        snake.appendleft((nx, ny)) # 머리 이동


        if apple and (nx, ny) in apple: # 다음 칸이 사과라면
           apple.remove((nx, ny)) # 사과 제거 - 처음 틀리고 추가
        else: # 다음 칸이 사과가 아니라면
            snake.pop()  # 꼬리 제거


        # 방향을 바꿔야하는 차례라면
        if m < L and cnt == move[m][0]:
            if move[m][1] == 'D': # 오른쪽 turn
                dir = (dir + 1 + 4) % 4
            else: # 왼쪽 turn
                dir = (dir - 1 + 4) % 4
            m += 1

    else:
        break

print(cnt)

