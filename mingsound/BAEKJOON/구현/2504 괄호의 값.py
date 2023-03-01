import sys
input = sys.stdin.readline

_str = list(input().rstrip())

stack = []
answer = 0 # 총합
tmp = 1 # 곱하기가 있어서 초기값 1로 설정

for i in range(len(_str)):
    if _str[i] == '(': # ( 열린 괄호면
        stack.append(_str[i])
        tmp *= 2 # 2를 곱해준다

    elif _str[i] == '[': # [ 열린 괄호면
        stack.append(_str[i])
        tmp *= 3 # 3을 곱해준다

    elif _str[i] == ')':
        if not stack or stack[-1] != '(': # 큐가 비어있거나, 짝이 맞지 않다면 - 올바르지 못한 괄호열
            answer = 0
            break

        if _str[i-1] == '(': # 가장 안쪽 괄호인 경우에만 answer에 값 더해주기
            answer += tmp
        stack.pop()  # 큐에서 맨 뒤 원소 제거 - 짝 맞는 괄호 제거
        tmp //= 2

    else: # _str[i] == ']'
        if not stack or stack[-1] != '[': # 큐가 비어있거나, 짝이 맞지 않다면 - 올바르지 못한 괄호열
            answer = 0
            break

        if _str[i-1] == '[':  # 가장 안쪽 괄호인 경우에만 answer에 값 더해주기
            answer += tmp
        stack.pop()  # 큐에서 맨 뒤 원소 제거 - 짝 맞는 괄호 제거
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)

# 2 x (2 + (3 x 3)) = (2 x 2) + (2 x (3 x 3))과 같이 생각을 하면 이해가 쉽다.
# 괄호 짝 맞추기 - 스택 자주 사용됨
