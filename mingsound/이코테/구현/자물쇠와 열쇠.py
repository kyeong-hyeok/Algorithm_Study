# 못품

# 요약
# 열쇠는 회전, 이동이 가능

# 핵심 idea
# 1. 두 개의 리스트를 겹쳐가는 범위를 다양하게 하면서 비교를 해야하는 경우, 밑판이 되는 리스트의 크기를 키우면 쉽게 범위 설정을 할 수 있다.
# 2. "1 - 0이 서로 짝이다." 서로 짝이되는 경우가 더해서 항상 같은 수가 나오는 경우라면, 두 개의 값을 더해서 판단 가능.


# key - lock 짝이 맞는지 확인하는 함수
def check(new_lock):
    n = len(new_lock) // 3
    # new_lock의 중앙 부분(= 실제 lock)을 모두 체크해서 다 1이면 key - lock 짝 맞는 것
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 중요! 기존 lock보다 3배 큰 자물쇠
    new_lock = [[0] * (n*3) for _ in range(n*3)]

    # 새로운 lock의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # key를 (1, 1)부터 (N*2, N*2)까지 이동시키며 확인
    for i in range(1, n*2):
        for j in range(1, n*2):
            for d in range(4): # 4방향 회전
                key = turn(key) # key 오른쪽으로 회전

                # lock의 (i, j)위치에서 key크기만큼 이중반복문 돌면서
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y] # key + lock

                # key와 lock이 짝이 맞는지 확인
                if check(new_lock):
                    return True

                # 다시 new_lock 원상 복구
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    return False

# key를 오른쪽으로 90도 회전
def turn(key):
    n = len(key)
    new_key = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_key[j][n-1-i] = key[i][j]

    return new_key
