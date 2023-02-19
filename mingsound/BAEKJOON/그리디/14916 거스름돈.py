# 2:57 - 3:10

n = int(input())

answer = 0
for i in range(n//5, -1, -1):
    N = n - (5 * i)
    if N % 2 == 0:
        answer = i + N // 2
        break

if answer == 0:
    print(-1)
else:
    print(answer)