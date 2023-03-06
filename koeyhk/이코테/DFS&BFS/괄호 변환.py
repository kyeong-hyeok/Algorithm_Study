from collections import deque


def correct(p):
    q = deque()
    for i in p:
        if i == '(':
            q.append(i)
        else:
            if not q:
                return False
            q.popleft()
    return True


def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]


def solution(p):
    if not p:
        return ""
    u, v = divide(p)
    if correct(u):
        return '' + u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer
