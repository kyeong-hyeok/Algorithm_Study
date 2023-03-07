from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 평행이동
def move(pos1, pos2, board):
    result = []
    x1, y1 = pos1
    x2, y2 = pos2
    for i in range(4): # 4방면으로 평행이동
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0: # 로봇의 두 칸이 모두 범위 안에 있다면
            result.append(((nx1, ny1), (nx2, ny2))) # result 배열에 추가

    return result

# 방향 체크
def is_horizontal(pos1, pos2):
    if pos1[0] == pos2[0]:
        return True # 가로 상태면 True 반환
    return False

# 회전
def turn(pos1, pos2, board):
    result = []
    if is_horizontal(pos1, pos2): # 가로라면
        x, y = pos1 # 왼쪽에 있는 것에 대해서
        if board[x+1][y] == 0 and board[x+1][y+1] == 0:# 아래 회전
            result.append((pos2, (x + 1, y + 1)))
        if board[x-1][y] == 0 and board[x-1][y+1] == 0:# 위 회전
            result.append(((x-1, y+1), pos2))

        x, y = pos2 # 오른쪽에 있는 것에 대해서
        if board[x+1][y] == 0 and board[x+1][y-1] == 0:# 아래 회전
            result.append((pos1, (x+1, y-1)))
        if board[x - 1][y] == 0 and board[x-1][y-1] == 0:# 위 회전
            result.append(((x-1, y-1), pos1))

    else: # 세로라면
        x, y = pos1 # 위에 있는 것에 대해서
        if board[x][y-1] == 0 and board[x+1][y-1] == 0:  # 왼쪽 회전
            result.append(((x + 1, y - 1), pos2))
        if board[x][y+1] == 0 and board[x+1][y+1] == 0:  # 오른쪽 회전
            result.append((pos2, (x + 1, y + 1)))

        x, y = pos2 # 아래 있는 것에 대해서
        if board[x][y-1] == 0 and board[x-1][y-1] == 0:  # 왼쪽 회전
            result.append(((x - 1, y - 1), pos1))
        if board[x][y+1] == 0 and board[x-1][y+1] == 0:  # 오른쪽 회전
            result.append((pos1, (x - 1, y + 1)))

    return result

# 또 다른 회전 방법
def turn2(pos1, pos2, new_board):
    result = []
    if is_horizontal(pos1, pos2):  # 가로방향 일 때
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            x1, y1 = pos1
            x2, y2 = pos2
            if new_board[x1 + d][y1] == 0 and new_board[x2 + d][y2] == 0: # pos2위치 고정일 때 대각선과, pos1위치 고정일 때 대각선이 0이라면
                # 위 if문에 and로 묶이면 안되는 것 아닌가 생각했지만, 저 두 칸이 각각 대각선 방향과 이동하려는 칸이라서 저렇게 묶여도 됨
                result.append((pos1, (x1 + d, y1))) # 왼쪽은 고정, 위와 아래로 로봇 칸 추가
                result.append((pos2, (x2 + d, y2))) # 오른쪽은 고정, 위와 아래로 로봇 칸 추가
    else:  # 세로 방향 일 때
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            x1, y1 = pos1
            x2, y2 = pos2
            if new_board[x1][y1 + d] == 0 and new_board[x2][y2 + d] == 0:
                result.append((pos1, (x1, y1 + d))) # pos1 고정, 좌우에 로봇 붙이기
                result.append((pos2, (x2, y2 + d))) # pos2 고정, 좌우에 로봇 붙이기
    return result

def solution(board):
    N = len(board) # 한 변 길이

    # board 테두리 1로 둘러싼 new_board 정의
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    # bfs
    queue = deque([((1, 1), (1, 2), 0)])
    visited = set([((1, 1), (1, 2))]) # 방문처리 set사용
    while queue:
        pos1, pos2, cnt = queue.popleft()
        if pos1 == (N, N) or pos2 == (N, N): # 로봇의 두 칸중 한 칸이라도 (N, N)에 도착했다면
            return cnt

        arr = move(pos1, pos2, new_board) # 평행이동해서 이동할 수 있는 위치를 담은 배열 arr
        for a in arr:
            if a not in visited: # 아직 해당 위치에 방문한 적 없다면
                new_pos1, new_pos2 = a
                queue.append((new_pos1, new_pos2, cnt + 1)) # 큐에 담기
                visited.add((new_pos1, new_pos2)) # 방문 처리

        arr = turn2(pos1, pos2, new_board) # 회전으로 이동할 수 있는 위치를 담은 배열 arr
        for a in arr:
            if a not in visited: # 아직 해당 위치에 방문한 적 없다면
                new_pos1, new_pos2 = a
                queue.append((new_pos1, new_pos2, cnt + 1)) # 큐에 담기
                visited.add((new_pos1, new_pos2)) # 방문 처리
