def solution(participant, completion):
    d = dict()      # 딕셔너리 생성
    for c in completion:
        if c in d:  # 완주한 선수 명단에 이름이 있다면 value + 1
            d[c] += 1
        else:       # 완주한 선수 명단에 이름이 없다면 value = 1로 넣기
            d[c] = 1
    for p in participant:
        if p not in d:      # 참가자들 중 완주한 선수 명단에 이름이 없다면
            return p
        else:               # 참가자들 중 완주한 선수 명단에 이름이 있다면 (동명이인 포함)
            if d[p] == 0:       # 해당 이름을 가진 완주한 선수가 없다면
                return p
            d[p] -= 1           # 해당 이름을 가진 완주한 선수의 value -1