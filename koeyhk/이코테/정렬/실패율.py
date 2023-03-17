def solution(N, stages):
    answer = []
    not_clear = [0] * N      # 해당 스테이지를 클리어하지 못한 플레이어 수
    reach = len(stages)    # 해당 스테이지에 도달한 플레이어 수
    fail = [[i+1, 0] for i in range(N)]     # [스테이지, 실패율]
    for i in stages:
        if i <= N:
            not_clear[i-1] += 1     # 클리어하지 못한 플레이어 +1
    for i in range(len(not_clear)):
        if reach != 0:      # 해당 스테이지에 도달한 사람이 있을 경우
            fail[i][1] = not_clear[i]/reach     # 실패율 구하기
            reach -= not_clear[i]   # 해당 스테이지까지만 도달한 사람 빼기
    fail.sort(key=lambda x: (-x[1], x[0]))  # 실패율 내림차순, 스테이지 오름차순 정렬
    for i in range(N):
        answer.append(fail[i][0])   # 스테이지 번호 차례대로 추가
    return answer