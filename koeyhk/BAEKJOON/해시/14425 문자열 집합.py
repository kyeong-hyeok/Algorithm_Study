import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
s = {input_data().rstrip() for _ in range(N)}
count = 0
for _ in range(M):
    ch = input_data().rstrip()
    if ch in s:
        count += 1
print(count)