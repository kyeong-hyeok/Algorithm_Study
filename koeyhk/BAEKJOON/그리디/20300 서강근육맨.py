import sys

N = int(input())
loss = list(map(int, sys.stdin.readline().split()))
loss.sort()
if N % 2 != 0:
    result = loss[N-1]
    for i in range(N//2):
        l = loss[i] + loss[N-2-i]
        result = l if l > result else result
else:
    result = loss[0] + loss[N-1]
    for i in range(1, N//2):
        l = loss[i] + loss[N-1-i]
        result = l if l > result else result
print(result)