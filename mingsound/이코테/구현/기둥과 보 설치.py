# 10:29 - 11:46

# 요약
# 기둥 : 바닥 / 보의 한쪽 끝 부분 위 / 다른 기둥 위
# 보 : 한쪽 끝이 기둥 위 / 양쪽 끝이 둘다 보
# 교차점 기준 기둥은 위, 보는 오른쪽에 설치
# x, y, a(0: 기둥, 1: 보), b(0: 삭제, 1: 설치)

# 설치, 삭제시 위의 조건에 맞지 않는다면 해당 작업 무시

# idea
# 설치 완료 구조물 (x, y, a)형태로 set에 저장
# 구조물 설치할 때 마다 set에 해당 경우 있는지 확인
build = set()

def check_pillar(x, y):
    if y == 0 or (x - 1, y, 1) in build or (x, y, 1) in build or (x, y - 1, 0) in build:
        return True
    else:
        return False

def check_boo(x, y):
    if (x, y - 1, 0) in build or (x + 1, y - 1, 0) in build or ((x - 1, y, 1) in build and (x + 1, y, 1) in build):
        return True
    else:
        return False

def solution(n, build_frame):
    # global build

    cnt = 0
    for cmd in build_frame:
        x, y = cmd[0], cmd[1]
        # 설치
        if cmd[3] == 1:
            if cmd[2] == 0: # 기둥
                if check_pillar(x, y):
                    build.add((x, y, 0))
            else: # 보
                if check_boo(x, y):
                    build.add((x, y, 1))

        # 삭제
        else:
            build.remove((x, y, cmd[2]))
            check = True

            # 전수 조사
            for b in build: 
                if b[2] == 0:
                    check &= check_pillar(b[0], b[1])
                else:
                    check &= check_boo(b[0], b[1])
            '''
            # 일부 조사
            if cmd[2] == 0:  # 기둥
                # 위에 기둥
                if (x, y + 1, 0) in build:
                    check &= check_pillar(x, y)
                # 위에 보 2개
                if (x-1, y+1, 1) in build:
                    check &= check_boo(x-1, y+1)
                if (x, y+1, 1) in build:
                    check &= check_boo(x, y+1)

            else:  # 보
                # 양 옆 보
                if (x-1, y, 1) in build:
                    check &= check_boo(x-1, y)
                if (x+1, y, 1) in build:
                    check &= check_boo(x+1, y)
                # 양 옆 위 기둥
                if (x, y, 0) in build:
                    check &= check_pillar(x, y)
                if (x+1, y, 0) in build:
                    check &= check_pillar(x+1, y)
            '''
            if not check:
                build.add((x, y, cmd[2]))

    return sorted(list(build), key = lambda x: (x[0], x[1], x[2]))

# 일부 조사 안되는 이유를 모르겠음...
