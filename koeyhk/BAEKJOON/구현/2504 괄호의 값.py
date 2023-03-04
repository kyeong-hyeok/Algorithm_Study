# () -> 2,   ( x ) -> 2 x 값(x)
# [] -> 3,   [ x ] -> 3 x 값(x)

N = input()
stack = []
result = 0
res = 1

for i in range(len(N)):
    if N[i] == '(':
        res *= 2
        stack.append(N[i])
    elif N[i] == '[':
        res *= 3
        stack.append(N[i])
    elif N[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if N[i-1] == '(':
            result += res
        res //= 2
        stack.pop()
    elif N[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if N[i-1] == '[':
            result += res
        res //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)