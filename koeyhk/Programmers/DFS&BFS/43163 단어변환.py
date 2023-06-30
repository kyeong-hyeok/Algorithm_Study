from collections import deque


def solution(begin, target, words):
    visited = [0] * len(words)      # 단어 변환 여부
    q = deque()
    q.append((begin, 0))            # (단어, 변환 횟수) 저장
    while q:
        w, a = q.popleft()
        if w == target:             # 현재 단어가 target일 때
            return a
        a += 1
        for i in range(len(words)):     # 단어 집합 words에 돌아가는 for문
            if visited[i] != 0:         # 변환한 단어라면
                continue
            diff = 0                    # 해당 단어와의 알파벳 차이 개수
            for j in range(len(w)):
                if w[j] != words[i][j]:     # 알파벳이 다르다면 diff += 1
                    diff += 1
                    if diff > 1:        # 다른 알파벳 개수가 1보다 크다면 break
                        break
            if diff <= 1:           # 다른 알파벳 개수가 1보다 작거나 같다면
                q.append((words[i], a))     # queue에 추가
                visited[i] = 1              # 변환 여부 갱신
    return 0
