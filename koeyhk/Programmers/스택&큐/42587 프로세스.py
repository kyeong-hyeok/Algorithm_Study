def solution(priorities, location):
    hl = sorted(priorities, reverse=True)       # 프로세스의 중요도를 내림차순 정렬한 리스트 생성
    visited = [0] * len(priorities)         # 프로세스 실행 여부
    c, mc = 0, 0        # 대기 큐의 인덱스, 내림차순 리스트의 인덱스
    while 1:
        if visited[c] == 0 and priorities[c] == hl[mc]:     # 실행하지 않았고, 다음에 실행될 프로세스라면
            if c == location:       # 알고싶은 프로세스의 위치라면
                return mc + 1
            visited[c] = 1      # 실행 여부 갱신
            mc += 1     # 다음 중요도를 가진 프로세스를 선택하기 위해 +1
        c = (c + 1) % len(priorities)       # 인덱스 값 초과 방지
