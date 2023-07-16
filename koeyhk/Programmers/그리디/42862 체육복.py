# 집합 사용 - 요소 접근 시간 단축

def solution(n, lost, reserve):
    res = set(reserve) - set(lost)
    los = set(lost) - set(reserve)
    for r in res:
        if r-1 in los:
            los.remove(r-1)
        elif r+1 in los:
            los.remove(r+1)
    return n - len(los)

# 학생의 수가 30명 이하 -> 시간 복잡도 고려하지 않고 풀 경우

def solution(n, lost, reserve):
    inx = 0
    while inx < len(lost):
        if lost[inx] in reserve:
            reserve.remove(lost[inx])
            del lost[inx]
        else:
            inx += 1
    lost.sort()
    reserve.sort()
    for r in reserve:
        for l in lost:
            if abs(r-l) == 1:
                lost.remove(l)
                break
    return n - len(lost)