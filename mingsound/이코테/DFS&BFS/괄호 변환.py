# 12:14 - 12:38

def change(p): # 괄호 방향 뒤집기
    p = list(p) # 문자열 type은 수정 불가능

    for i in range(len(p)): # 괄호 방향 뒤집기
        p[i] = '(' if p[i] == ')' else ')'

    return ''.join(p) # 다시 문자열 형태로 반환


def solution(p):
    if p == '': # 빈 문자열이면 빈 문자열 반환
        return ''

    open = close = 0 # 열린괄호 갯수, 닫힌 괄호 갯수
    correct = True # 올바른 괄호 문자열 여부

    for i in range(len(p)):
        if p[i] == '(': # 열린 괄호 갯수 + 1
            open += 1
        else: # 닫힌 괄호 갯수 + 1
            close += 1

        if close > open: # 닫힌괄호가 더 많은 순간이 있다면, 올바르지 않은 문자열
            correct = False
        elif open == close: # 더 이상 균형잡힌 괄호 문자열로 분리할 수 없는 상황
            break

    # u, v 분리
    u = p[:i+1]
    v = p[i+1:]


    if correct: # u가 올바른 괄호 문자열인 경우
        answer = u + solution(v)
    else: # u가 올바르지 않은 괄호 문자열인 경우
        answer = "(" + solution(v) + ")" + change(u[1:-1])

    return answer